def add_point(discord_id: str, conn):
    conn.execute(
        "INSERT OR IGNORE INTO users (discord_id, points) VALUES (?, 0)",
        (discord_id,)
    )
    conn.execute(
        "UPDATE users SET points = points + 1 WHERE discord_id = ?",
        (discord_id,)
    )
    conn.commit()

def get_points(discord_id: str, conn):
    cur = conn.execute(
        "SELECT points FROM users WHERE discord_id = ?",
        (discord_id,)
    )
    row = cur.fetchone()
    return row[0] if row else 0
