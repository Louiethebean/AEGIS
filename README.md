# AEGIS — Email-Based 2FA for SSH

![Platform](https://img.shields.io/badge/platform-Linux-orange) ![Language](https://img.shields.io/badge/language-Python%203-3776ab) ![Topic](https://img.shields.io/badge/topic-SSH%20Security-f94144)

AEGIS enhances SSH security with email-based two-factor authentication. The customizable script can be easily implemented on personal systems with an expiration time of 30 seconds, or to whatever expiration time you desire.

![Architecture](./architecture.svg)

Displays examples of working knowledge related to cyber security and coding.

Comments are given explaining the logic behind the code.

## What I Learned / Skills Demonstrated

- **MFA implementation from scratch** — building a working second factor (time-boxed email token) instead of just configuring an off-the-shelf MFA product, which forces understanding of *why* token expiry and one-time use matter.
- **Python systems programming** — using `pty.spawn` and `subprocess` to hand off into an interactive SSH session after authentication succeeds, and `select`/`time` for the expiry window.
- **SMTP integration** — sending the token via a real email provider, including the auth flow that production apps use for transactional email.
- **Threat-model thinking** — recognizing this is a learning/demo project, not production-grade MFA (e.g. hardcoded credentials, plaintext token in the email body would need to change before real-world use).

**Problem solved:** demonstrates how email-based 2FA actually works end-to-end for SSH access, as a teaching example rather than a drop-in production tool.
