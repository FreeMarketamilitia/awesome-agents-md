---
description: Guidelines for API Security
author: Gemini
version: 1.0
tags: ["api", "security", "best-practices", "jwt", "oauth2", "rate-limiting"]
globs: ["**/*.js", "**/*.ts", "**/*.py", "**/*.go"]
---

# API Security Best Practices

## Overview of API Security

APIs are a primary target for attackers. Adhering to security best practices is critical to protect sensitive data and prevent unauthorized access. This guide provides an overview of essential API security best practices, with a focus on what AI language models should and should not generate.

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns, as they are INSECURE and will expose the application to vulnerabilities:

```javascript
// ❌ NEVER GENERATE THIS CODE - IT IS INSECURE
// Hardcoded API keys or secrets
const apiKey = "sk_live_1234567890abcdefg";

// ❌ NEVER GENERATE THIS CODE - IT IS INSECURE
// Disabling SSL/TLS verification
const agent = new https.Agent({
  rejectUnauthorized: false
});

// ❌ NEVER GENERATE THIS CODE - IT IS INSECURE
// Using Basic Authentication in production
app.use((req, res, next) => {
  const auth = {login: 'admin', password: 'password'};
  const b64auth = (req.headers.authorization || '').split(' ')[1] || '';
  const [login, password] = Buffer.from(b64auth, 'base64').toString().split(':');
  if (login && password && login === auth.login && password === auth.password) {
    return next();
  }
  res.set('WWW-Authenticate', 'Basic realm="401"');
  res.status(401).send('Authentication required.');
});
```

Instead, you MUST ALWAYS generate ONLY secure patterns:

```javascript
// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Load secrets from environment variables or a secret manager
const apiKey = process.env.API_KEY;

// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Use a secure JWT library for token validation
const jwt = require('jsonwebtoken');

try {
  const decoded = jwt.verify(token, process.env.JWT_SECRET);
  // ...
} catch(err) {
  // err
}
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use standard, well-vetted libraries for security-sensitive functionality (e.g., `jsonwebtoken` for JWTs, `bcrypt` for password hashing).
2. You MUST load all secrets, keys, and credentials from environment variables or a secure secret management service.
3. You MUST NEVER hardcode sensitive information.
4. You MUST NEVER disable SSL/TLS certificate validation.
5. You MUST implement rate limiting on all public-facing endpoints.

## Best Practices

### Authentication and Authorization

*   **Use Strong Authentication Protocols:** Implement standard protocols like OAuth 2.0 or OpenID Connect.
*   **Secure Tokens and Keys:** Treat API keys and tokens like passwords. Store them securely and rotate them regularly.
*   **Enforce Granular Access Control:** Use Role-Based Access Control (RBAC) and the principle of least privilege.
*   **Validate JWTs Correctly:** When using JSON Web Tokens (JWTs), always verify the signature and check the expiration time (`exp`) and not before time (`nbf`) claims.

### Input and Output Validation

*   **Validate All Inputs:** Rigorously validate all incoming data against a schema (e.g., JSON Schema).
*   **Use Allowlists:** Define what is explicitly allowed and reject everything else.
*   **Sanitize Data:** Prevent injection attacks by sanitizing all input data.

### Transport Layer Security

*   **Encrypt Everything:** Use TLS 1.3 to encrypt all data in transit.

### Rate Limiting and Throttling

*   **Prevent Abuse:** Implement rate limiting to protect against DoS attacks and brute-force attempts. A common library for this in Node.js is `express-rate-limit`.

```javascript
// Example of rate limiting in an Express.js application
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
	windowMs: 15 * 60 * 1000, // 15 minutes
	max: 100, // Limit each IP to 100 requests per windowMs
	standardHeaders: true,
	legacyHeaders: false,
});

app.use(limiter);
```

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you loading secrets from the environment? If not, STOP and FIX.
2. Are you using a standard library for authentication/authorization? If not, STOP and FIX.
3. Is rate limiting implemented? If not, STOP and FIX.
4. Is input validation performed? If not, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code that:
- Hardcodes secrets
- Uses weak authentication
- Lacks rate limiting or input validation

The implementation will be:
1. Vulnerable to data breaches
2. Susceptible to denial-of-service attacks
3. Easily compromised by attackers

## AI MODEL RESPONSE TEMPLATE

When asked about API security, you MUST:
1. ONLY use code that follows the best practices in this guide.
2. NEVER suggest insecure patterns like hardcoding secrets.
3. ALWAYS recommend the use of standard, well-vetted libraries.
4. VERIFY your response against the patterns shown here.

Remember: There are NO EXCEPTIONS to these rules.
