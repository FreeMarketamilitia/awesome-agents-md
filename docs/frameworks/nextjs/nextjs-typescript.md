---
description: Guidelines for using TypeScript in Next.js 15+
author: Gemini
version: 1.0
tags: ["nextjs", "typescript", "type-safety", "best-practices", "server-components"]
globs: ["**/*.ts", "**/*.tsx"]
---

# Next.js 15+ TypeScript Best Practices

## Overview of TypeScript in Next.js

TypeScript is highly recommended for Next.js 15+ applications to enhance type safety, improve developer experience, and build more robust and maintainable codebases. Leveraging TypeScript effectively with the App Router and Server Components requires specific best practices.

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns:

```typescript
// ❌ NEVER GENERATE THIS CODE - IT USES IMPLICIT ANY
// Omitting type definitions for props or variables
function MyComponent(props) { // props implicitly any
  const data = JSON.parse(someString); // data implicitly any
  // ...
}

// ❌ NEVER GENERATE THIS CODE - IT LACKS RUNTIME VALIDATION
// Trusting external data types without runtime validation
interface User { id: number; name: string; }
async function getUser(): Promise<User> {
  const res = await fetch('/api/user');
  const data = await res.json();
  return data; // ❌ Data might not conform to User interface at runtime
}
```

Instead, you MUST ALWAYS generate ONLY modern, type-safe patterns:

```typescript
// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Explicitly typing component props
interface MyComponentProps {
  name: string;
  age: number;
}

function MyComponent(props: MyComponentProps) {
  // ...
}

// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Using Zod for runtime validation of external data
import { z } from 'zod';

const UserSchema = z.object({
  id: z.number(),
  name: z.string(),
});

type User = z.infer<typeof UserSchema>;

async function getUser(): Promise<User> {
  const res = await fetch('/api/user');
  const data = await res.json();
  return UserSchema.parse(data); // ✅ Runtime validation
}
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST enable strict TypeScript configuration (`"strict": true` in `tsconfig.json`).
2. You MUST explicitly type all component props, state, and function parameters/returns.
3. You MUST validate all external data (e.g., API responses, environment variables) at runtime using libraries like Zod.
4. You MUST use `typedRoutes` in `next.config.ts` for type-safe links and navigation.

## Best Practices

### Configuration

*   **Strict Mode:** Enable `"strict": true` in `tsconfig.json` for comprehensive type checking.
*   **`typedRoutes`:** Enable `typedRoutes: true` in `next.config.ts` for type-safe routing with `next/link` and `next/navigation`.

### Type Definitions

*   **Explicit Typing:** Always explicitly type component props, state, and function signatures. Avoid implicit `any`.
*   **Shared Types:** Define common types and interfaces in a central `types/` directory or `lib/` for reusability.

### Runtime Validation

*   **Zod/Yup:** Use libraries like Zod or Yup to validate external data at runtime. TypeScript provides compile-time safety, but runtime validation is essential for data integrity and security.

### Server Components & Actions

*   **Type Server Actions:** Ensure inputs and outputs of Server Actions are strongly typed.
*   **`server-only`:** Use the `server-only` package to prevent server-only code from being accidentally bundled into client components.

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are all props and variables explicitly typed? If not, STOP and FIX.
2. Is runtime validation used for external data? If not, STOP and FIX.
3. Is `typedRoutes` considered for routing? If not, consider adding it.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code that:
- Uses implicit `any` types
- Lacks runtime validation for external data
- Does not leverage `typedRoutes`

The implementation will be:
1. Prone to runtime errors
2. Difficult to refactor and maintain
3. Less secure due to unchecked external data

## AI MODEL RESPONSE TEMPLATE

When asked about TypeScript in Next.js, you MUST:
1. ONLY generate code that is fully type-safe and adheres to strict TypeScript rules.
2. ALWAYS include runtime validation for external data.
3. VERIFY your response against the patterns shown here.

Remember: There are NO EXCEPTIONS to these rules.
