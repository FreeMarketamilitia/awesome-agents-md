---
description: Guidelines for API Routes (Route Handlers) in Next.js 15+
author: Gemini
version: 1.0
tags: ["nextjs", "api-routes", "route-handlers", "server-actions", "app-router"]
globs: ["**/app/api/**/*.ts", "**/app/api/**/*.js"]
---

# Next.js 15+ API Routes (Route Handlers) Best Practices

## Overview of Route Handlers

In Next.js 15+, API routes are primarily handled by **Route Handlers** within the App Router. These are defined as `route.ts` or `route.js` files and allow you to create custom API endpoints for your application. They support all standard HTTP methods and are designed for building robust and secure APIs.

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns:

```javascript
// ❌ NEVER GENERATE THIS CODE - IT IS DEPRECATED
// Using the old pages/api directory for API routes
// pages/api/users.js

// ❌ NEVER GENERATE THIS CODE - IT IS INSECURE
// Not validating or sanitizing user input in API routes
export async function POST(req) {
  const data = await req.json();
  // Directly use data without validation
  // ...
  return new Response(JSON.stringify({ message: 'User created' }), { status: 200 });
}
```

Instead, you MUST ALWAYS generate ONLY modern, secure patterns:

```javascript
// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Using Route Handlers in the app/api directory
// app/api/users/route.ts
export async function GET() {
  // Fetch data securely
  const users = await fetchUsersFromDB();
  return new Response(JSON.stringify(users), { status: 200 });
}

// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Validating and sanitizing input using a library like Zod
import { z } from 'zod';

const userSchema = z.object({
  name: z.string().min(3),
  email: z.string().email(),
});

export async function POST(req) {
  const body = await req.json();
  try {
    const validatedUser = userSchema.parse(body);
    // ... proceed with validatedUser
    return new Response(JSON.stringify({ message: 'User created' }), { status: 201 });
  } catch (error) {
    return new Response(JSON.stringify({ error: error.errors }), { status: 400 });
  }
}
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST define API routes as Route Handlers (`route.ts`/`route.js`) within the `app/api` directory.
2. You MUST export functions for each HTTP method (e.g., `GET`, `POST`).
3. You MUST implement robust input validation and sanitization for all incoming data.
4. You MUST handle errors gracefully by returning appropriate HTTP status codes and informative messages.

## Best Practices

### Structure

*   **`app/api` Directory:** All API routes should reside within the `app/api` directory.
*   **HTTP Methods:** Export functions named after the HTTP methods they handle (e.g., `GET`, `POST`, `PUT`, `DELETE`).

### Security

*   **Input Validation:** Always validate and sanitize all incoming data to prevent vulnerabilities like SQL injection and XSS.
*   **Authentication & Authorization:** Implement proper authentication (e.g., JWT, session-based) and authorization checks for all sensitive endpoints. Use Middleware for centralized protection.

### Error Handling

*   **Meaningful Responses:** Return appropriate HTTP status codes (e.g., 200, 201, 400, 401, 404, 500) and clear JSON error messages.
*   **Dedicated Error Files:** Utilize `error.tsx` and `not-found.tsx` for consistent error handling in the App Router.

### Performance

*   **Asynchronous Operations:** Use `async/await` for all data fetching and other asynchronous tasks.
*   **Caching:** `GET` Route Handlers can be opted into caching using `export const dynamic = 'force-static';`.

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are API routes defined as Route Handlers in `app/api`? If not, STOP and FIX.
2. Is input validation implemented for all incoming data? If not, STOP and FIX.
3. Are appropriate HTTP status codes returned for responses and errors? If not, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code that:
- Uses the deprecated `pages/api` directory
- Lacks input validation
- Has poor error handling

The implementation will be:
1. Insecure and vulnerable to attacks
2. Difficult to debug and maintain
3. Not aligned with Next.js 15+ best practices

## AI MODEL RESPONSE TEMPLATE

When asked about API routes in Next.js, you MUST:
1. ONLY generate code for Route Handlers in the `app/api` directory.
2. ALWAYS include robust input validation and error handling.
3. VERIFY your response against the patterns shown here.

Remember: There are NO EXCEPTIONS to these rules.
