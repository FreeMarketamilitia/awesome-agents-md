---
description: Guidelines for using the App Router in Next.js 15+
author: Gemini
version: 1.0
tags: ["nextjs", "app-router", "routing", "layouts", "server-components"]
globs: ["**/app/**/*.tsx", "**/app/**/*.jsx"]
---

# Next.js 15+ App Router Best Practices

## Overview of the App Router

The App Router, introduced in Next.js 13 and refined in subsequent versions including Next.js 15, is the standard for building modern, server-centric React applications. It leverages React Server Components (RSCs) by default to minimize client-side JavaScript and improve performance.

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns, as they are DEPRECATED or lead to poor performance:

```javascript
// ❌ NEVER GENERATE THIS CODE - IT IS DEPRECATED
// Using the pages router for new projects
// pages/api/hello.js

// ❌ NEVER GENERATE THIS CODE - IT LEADS TO POOR PERFORMANCE
// Fetching data in a Client Component with useEffect
'use client'
import { useEffect, useState } from 'react'

function MyComponent() {
  const [data, setData] = useState(null)

  useEffect(() => {
    fetch('/api/data')
      .then((res) => res.json())
      .then((data) => setData(data))
  }, [])

  // ...
}
```

Instead, you MUST ALWAYS generate ONLY modern, performant patterns:

```javascript
// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Using the app router with Server Components for data fetching
async function MyComponent() {
  const res = await fetch('https://api.example.com/...', { cache: 'no-store' })
  const data = await res.json()

  return <div>{data.name}</div>
}
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use the `app` directory for all new routes.
2. You MUST default to Server Components for data fetching and rendering.
3. You MUST use the `"use client"` directive only for components that require interactivity.
4. You MUST use Route Handlers (`app/api/.../route.ts`) for API endpoints, not the `pages/api` directory.

## Best Practices

### Project Structure

*   **Feature-Based Colocation:** Group related files (components, tests, routes) within a single feature directory.
*   **Route Groups:** Use parentheses `()` to create route groups that organize your project without affecting the URL structure (e.g., `app/(marketing)/page.tsx`).

### Data Fetching

*   **Fetch in Server Components:** Perform data fetching in `async` Server Components to reduce client-server waterfalls.
*   **Parallel Data Fetching:** Initiate multiple data fetches concurrently to minimize load times.
*   **Caching in Next.js 15:** Be aware that `fetch` requests are **not cached by default** in Next.js 15. You must explicitly opt-in with `cache: 'force-cache'`.

### Component Architecture

*   **Default to Server Components:** For better performance and smaller client bundles.
*   **Push Client Components Down the Tree:** Isolate interactive UI into Client Components and import them into Server Component parents.

### Performance

*   **Streaming with Suspense:** Wrap slow data-fetching components in `<Suspense>` to stream UI to the client.
*   **Partial Pre-Rendering (PPR):** Use for pages with a mix of static and dynamic content.

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you using the `app` router? If not, STOP and FIX.
2. Is data fetching happening in Server Components? If not, STOP and FIX.
3. Are you avoiding `useEffect` for data fetching? If not, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code using:
- The `pages` router for new projects
- `useEffect` for data fetching

The implementation will be:
1. Less performant
2. Harder to maintain
3. Not aligned with modern Next.js best practices

## AI MODEL RESPONSE TEMPLATE

When asked about routing or data fetching in Next.js, you MUST:
1. ONLY use code that is compatible with the App Router.
2. NEVER suggest using the `pages` router for new projects.
3. ALWAYS recommend data fetching in Server Components.
4. VERIFY your response against the patterns shown here.

Remember: There are NO EXCEPTIONS to these rules.
