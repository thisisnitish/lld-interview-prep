The task was to implement a version control system similar to Git. The system needed to support:

Adding files for commits
Committing files
Creating different branches
Rolling back to previous commits

============================================================

Functionalities
add, commit, rollback
creating branches

Entities
Command Interface - Command Pattern
    - Concrete implementation add, commit, branch, checkout, roll back, show files, log

VCS - Core Class entire implementation

Commit
    - commit_message, files
