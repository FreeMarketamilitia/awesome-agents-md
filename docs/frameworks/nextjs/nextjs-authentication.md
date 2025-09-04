---
description: Guidelines for Authentication in Next.js 15+
author: Gemini
version: 1.0
tags: ["nextjs", "authentication", "authjs", "next-auth", "middleware", "server-actions"]
globs: ["**/app/**/*.tsx", "**/app/**/*.jsx", "middleware.ts", "auth.config.ts"]
---

# Next.js 15+ Authentication Best Practices

## Overview of Authentication

Authentication in Next.js 15+ should be handled on the server using Middleware, Server Components, and Server Actions. The recommended library for this is Auth.js (formerly NextAuth.js), which simplifies complex authentication flows and provides robust security features out of the box.

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns:

```javascript
// ❌ NEVER GENERATE THIS CODE - IT IS INSECURE
// Storing session tokens in localStorage
const token = localStorage.getItem('token');

// ❌ NEVER GENERATE THIS CODE - IT IS INSECURE
// Performing authentication checks on the client-side only
'use client'
import { useSession } from 'next-auth/react'

function MyComponent() {
  const { data: session } = useSession()
  if (!session) return null // ❌ INSECURE - Hides UI but doesn't protect the route
  // ...
}
```

Instead, you MUST ALWAYS generate ONLY modern, secure patterns:

```javascript
// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Protecting routes with Middleware
// middleware.ts
export { auth as middleware } from "@/auth"
export const config = {
  matcher: ["/dashboard/:path*"],
}

// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Fetching session data in a Server Component
import { auth } from "@/auth"

async function MyComponent() {
  const session = await auth()
  // ...
}

// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Protecting a Server Action
'use server'
import { auth } from "@/auth"

export async function myAction() {
  const session = await auth()
  if (!session?.user) {
    throw new Error("Unauthorized")
  }
  // ...
}
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use a dedicated authentication library like Auth.js.
2. You MUST use Middleware to protect routes.
3. You MUST perform authentication checks in Server Components and Server Actions.
4. You MUST store session tokens in `httpOnly`, `secure` cookies (which Auth.js does by default).

## Best Practices

### Route Protection

*   **Middleware:** Use `middleware.ts` to protect routes. This is the most efficient and secure way to handle route protection.

### Session Management

*   **Server Components:** Fetch session data in Server Components using `await auth()`.
*   **Server Actions:** Always check for an active session at the beginning of any Server Action that performs a mutation.

### Security

*   **`httpOnly` Cookies:** Ensure session tokens are stored in `httpOnly` cookies to prevent access from client-side JavaScript.
*   **CSRF Protection:** Use a library like Auth.js that has built-in CSRF protection.

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you using Middleware for route protection? If not, STOP and FIX.
2. Are authentication checks performed on the server (Server Components/Actions)? If not, STOP and FIX.
3. Are you using a reputable authentication library? If not, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code that:
- Relies on client-side authentication checks
- Stores tokens in `localStorage`

The implementation will be:
1. Vulnerable to XSS and CSRF attacks
2. Easily bypassed by attackers
3. A major security risk

## AI MODEL RESPONSE TEMPLATE

When asked about authentication in Next.js, you MUST:
1. ONLY generate code that uses server-side authentication checks.
2. ALWAYS recommend using Middleware for route protection.
3. STRONGLY recommend using Auth.js or a similar library.
4. VERIFY your response against the patterns shown here.

Remember: There are NO EXCEPTIONS to these rules.
