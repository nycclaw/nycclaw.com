interface Env {
  DB: D1Database;
}

interface SubscribeBody {
  email: string;
  name?: string;
  type?: string;
  source?: string;
}

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': 'https://nycclaw.com',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

// Simple in-memory rate limiter (per-isolate, resets on cold start)
const rateLimitMap = new Map<string, number[]>();
const RATE_LIMIT_WINDOW_MS = 60_000; // 1 minute
const RATE_LIMIT_MAX = 5; // 5 requests per minute per IP

function isRateLimited(ip: string): boolean {
  const now = Date.now();
  const timestamps = rateLimitMap.get(ip) || [];
  const recent = timestamps.filter((t) => now - t < RATE_LIMIT_WINDOW_MS);
  if (recent.length >= RATE_LIMIT_MAX) return true;
  recent.push(now);
  rateLimitMap.set(ip, recent);
  return false;
}

function isValidEmail(email: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) && email.length <= 254;
}

export const onRequestPost: PagesFunction<Env> = async (context) => {
  const ip = context.request.headers.get('CF-Connecting-IP') || 'unknown';

  if (isRateLimited(ip)) {
    return Response.json(
      { error: 'Too many requests. Please try again later.' },
      { status: 429, headers: CORS_HEADERS }
    );
  }

  let body: SubscribeBody;
  try {
    body = await context.request.json();
  } catch {
    return Response.json(
      { error: 'Invalid JSON body.' },
      { status: 400, headers: CORS_HEADERS }
    );
  }

  const email = body.email?.trim().toLowerCase();
  if (!email || !isValidEmail(email)) {
    return Response.json(
      { error: 'Please provide a valid email address.' },
      { status: 400, headers: CORS_HEADERS }
    );
  }

  const type = body.type || 'newsletter';
  const source = body.source || 'unknown';
  const name = body.name?.trim() || null;

  try {
    await context.env.DB.prepare(
      'INSERT INTO subscribers (email, name, type, source) VALUES (?, ?, ?, ?)'
    )
      .bind(email, name, type, source)
      .run();

    return Response.json(
      { message: "You're subscribed! Welcome to the NYC Claw community." },
      { status: 201, headers: CORS_HEADERS }
    );
  } catch (err: any) {
    // D1 unique constraint error
    if (err?.message?.includes('UNIQUE constraint failed')) {
      return Response.json(
        { message: "You're already subscribed!" },
        { status: 200, headers: CORS_HEADERS }
      );
    }
    return Response.json(
      { error: 'Something went wrong. Please try again.' },
      { status: 500, headers: CORS_HEADERS }
    );
  }
};

export const onRequestOptions: PagesFunction = async () => {
  return new Response(null, { status: 204, headers: CORS_HEADERS });
};
