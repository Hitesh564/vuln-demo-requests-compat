# Vulnerable Requests Compatibility Fixture

Controlled public acceptance fixture for the Autonomous Vulnerability Remediation Agent.

The application intentionally contains a strict dependency compatibility guard.

Baseline:

- Requests 2.32.3 is installed.
- Application tests pass.

During remediation:

- OSV identifies the vulnerable dependency.
- The agent upgrades Requests to a fixed version.
- The old compatibility guard rejects the new dependency version.
- Tests fail.
- The agent must diagnose the dependency compatibility failure.
- A code-repair model updates the application compatibility logic.
- Tests are executed again.
- OSV is independently re-queried.

The compatibility constraint is intentionally included to exercise the agent's
self-correction workflow. It is not intended to represent a production application.
