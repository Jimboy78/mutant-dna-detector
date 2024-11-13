import sqlite3


def init_db():
    conn = sqlite3.connect('dna_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS dna_sequences (
                    sequence TEXT PRIMARY KEY,
                    is_mutant BOOLEAN
                 )''')
    conn.commit()
    conn.close()


def store_dna(dna, is_mutant):
    conn = sqlite3.connect('dna_data.db')
    c = conn.cursor()
    sequence = ''.join(dna)
    c.execute('INSERT OR IGNORE INTO dna_sequences (sequence, is_mutant) VALUES (?, ?)', (sequence, is_mutant))
    conn.commit()
    conn.close()


def get_stats():
    conn = sqlite3.connect('dna_data.db')
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM dna_sequences WHERE is_mutant = 1')
    count_mutant = c.fetchone()[0]
    c.execute('SELECT COUNT(*) FROM dna_sequences WHERE is_mutant = 0')
    count_human = c.fetchone()[0]
    conn.close()

    total = count_mutant + count_human
    ratio = count_mutant / total if total > 0 else 0

    return {
        "count_mutant_dna": count_mutant,
        "count_human_dna": count_human,
        "ratio": ratio
    }


init_db()
