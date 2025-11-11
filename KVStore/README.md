Key Value Store


Requirements:

Functional Requirements:
SET key value
Stores the key with the given value. If key exists, overwrite it.

GET key
Returns the value associated with the key. Return None or an error if key doesn’t exist.

DELETE key
Removes the key from the store.

COUNT value
Returns the number of keys that have the given value.

BEGIN
Starts a new transaction.

ROLLBACK
Rolls back the most recent transaction.

COMMIT
Commits all open transactions.


🔧 Constraints
Must work in-memory only (no disk persistence).
Support nested transactions (BEGIN can be called multiple times). - tentative
All operations should have constant or logarithmic time complexity.
Use clean, modular, and maintainable code.

=====================================================================================
KVStore => Singleton class
- Txns
Commands => Command Pattern
    - Command Factory
