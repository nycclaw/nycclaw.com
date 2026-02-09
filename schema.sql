CREATE TABLE IF NOT EXISTS subscribers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL UNIQUE,
  name TEXT,
  type TEXT NOT NULL DEFAULT 'newsletter', -- newsletter | discovery | waitlist
  source TEXT, -- hero | community | footer
  metadata TEXT, -- JSON blob for extra fields
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_subscribers_email ON subscribers(email);
CREATE INDEX IF NOT EXISTS idx_subscribers_type ON subscribers(type);
