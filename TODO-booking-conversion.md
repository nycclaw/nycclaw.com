# Booking Conversion Tracking — TODO

**Status:** Not started
**Priority:** Medium
**Created:** 2026-03-22

## Problem
GA4 Measurement Protocol events fired server-side from the Cal.com webhook worker are silently dropped by GA4 because there's no active browser session. The `booking_confirmed` event never appears in reports.

## Solution (Recommended)
Build a thank-you page at `/booking-confirmed` on nycclaw.com:

1. **Create `/booking-confirmed` page** — simple confirmation with next-steps messaging
2. **Fire gtag conversion event** client-side on page load (`booking_confirmed`, with source/value params)
3. **Set Cal.com redirect URL** to `https://nycclaw.com/booking-confirmed?source={eventType}`
4. **Optionally mark as GA4 conversion** in the GA4 admin

## Future Enhancement
- Embed Cal.com booking widget directly on nycclaw.com instead of linking out
- Listen for `bookingSuccessful` postMessage event → fire gtag from parent page
- Better UX (user stays on site) + same conversion tracking benefit

## Context
- GA4 property: `G-DBW292SFKX` (nycclaw.com, property 529122140)
- CF Worker (`calcom-webhook`): still sends MP event as backup, but it's unreliable alone
- MP API secret + measurement ID confirmed valid via debug endpoint
- Cal.com webhook template paths were also fixed today (2026-03-22) — `{{payload.X}}` → `{{payload.payload.X}}`
- Webhook subscription trimmed to only BOOKING_CREATED, BOOKING_RESCHEDULED, BOOKING_CANCELLED
