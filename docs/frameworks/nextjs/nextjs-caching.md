---
description: Guidelines for Caching in Next.js 15+
author: Gemini
version: 1.0
tags: ["nextjs", "caching", "data-fetching", "performance", "revalidation"]
globs: ["**/app/**/*.tsx", "**/app/**/*.jsx", "next.config.mjs"]
---

# Next.js 15+ Caching Best Practices

## Overview of Caching

Next.js 15 introduces a major shift in caching philosophy. It moves from a "cached-by-default" model to an explicit "opt-in" system. This gives developers more control and predictability. Understanding how to use the new `cache` option on `fetch` and the `unstable_cache` function is essential for building performant applications.

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns:

```javascript
// ❌ NEVER GENERATE THIS CODE - IT RELIES ON OLD DEFAULTS
// Omitting the `cache` option on a fetch call
const res = await fetch('https://api.example.com/...') // ❌ RELIES ON OLD CACHING BEHAVIOR

// ❌ NEVER GENERATE THIS CODE - IT IS INEFFICIENT
// Manually implementing a cache with useState/useEffect
'use client'
import { useEffect, useState } from 'react'
let cache = new Map()
function MyComponent({ id }) {
  const [data, setData] = useState(cache.get(id))
  useEffect(() => {
    if (!data) {
      fetch(`/api/data/${id}`)
        .then(res => res.json())
        .then(d => {
          cache.set(id, d)
          setData(d)
        })
    }
  }, [id, data])
}
```

Instead, you MUST ALWAYS generate ONLY modern, performant patterns:

```javascript
// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Explicitly setting the cache option on a fetch call
const res = await fetch('https://api.example.com/...', { cache: 'force-cache' })

// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Using unstable_cache for non-fetch operations
import { unstable_cache } from 'next/cache'
import { db } from './db'

export const getUser = unstable_cache(
  async (userId) => db.getUser(userId),
  ['users'],
  { tags: ['user'] }
)
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST explicitly set the `cache` option on all `fetch` calls.
2. You MUST use `unstable_cache` for caching the results of database queries or other non-`fetch` async functions.
3. You MUST use tag-based revalidation (`revalidateTag`) for on-demand cache invalidation.
4. You MUST NOT rely on the old, implicit caching behavior of Next.js 14 and below.

## Best Practices

### Caching Strategies

*   **`cache: 'force-cache'`**: For static data that should be cached indefinitely.
*   **`cache: 'no-store'`**: To opt out of caching and fetch data on every request.
*   **`next: { revalidate: number }`**: For time-based revalidation (e.g., `revalidate: 3600` for one hour).

### On-Demand Revalidation

*   **Tagging Data:** Use the `tags` option in `unstable_cache` or `fetch` to associate cached data with a specific tag.
*   **Invalidating Tags:** Use `revalidateTag` in a Server Action or API Route to invalidate all data associated with a tag.

### Caching Non-`fetch` Operations

*   **`unstable_cache`:** Wrap database queries, CMS calls, or any other async function that doesn't use `fetch` with `unstable_cache` to cache its results.

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Is the `cache` option explicitly set on every `fetch` call? If not, STOP and FIX.
2. Are you using `unstable_cache` for non-`fetch` data sources? If not, STOP and FIX.
3. Are you using tags for on-demand revalidation? If not, consider adding them.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code that:
- Omits the `cache` option on `fetch`
- Does not use `unstable_cache` for database calls

The implementation will:
1. Behave unpredictably as caching defaults may change.
2. Be inefficient and make unnecessary requests.
3. Be difficult to manage and debug.

## AI MODEL RESPONSE TEMPLATE

When asked about caching in Next.js, you MUST:
1. ONLY generate code that explicitly sets the caching strategy.
2. ALWAYS use `unstable_cache` for non-`fetch` data.
3. RECOMMEND tag-based revalidation for dynamic data.
4. VERIFY your response against the patterns shown here.

Remember: There are NO EXCEPTIONS to these rules.
