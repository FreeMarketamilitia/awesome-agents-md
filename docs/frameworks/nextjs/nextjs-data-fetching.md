---
description: Guidelines for Data Fetching in Next.js 15+
author: Gemini
version: 1.0
tags: ["nextjs", "data-fetching", "server-components", "caching", "suspense"]
globs: ["**/app/**/*.tsx", "**/app/**/*.jsx"]
---

# Next.js 15+ Data Fetching Best Practices

## Overview of Data Fetching

In Next.js 15+, data fetching is primarily done in Server Components. This server-first approach improves performance and security. Understanding the new caching defaults and patterns like parallel fetching and streaming is crucial.

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns:

```javascript
// ❌ NEVER GENERATE THIS CODE - IT IS INEFFICIENT
// Fetching data in a Client Component with useEffect for initial render
'use client'
import { useEffect, useState } from 'react'

function MyComponent() {
  const [data, setData] = useState(null)

  useEffect(() => {
    fetch('/api/data').then(res => res.json()).then(setData)
  }, [])
  // ...
}

// ❌ NEVER GENERATE THIS CODE - IT CREATES WATERFALLS
// Sequentially awaiting fetches that could be parallelized
async function MyComponent() {
  const artists = await getArtists();
  const albums = await getAlbums();
  // ...
}
```

Instead, you MUST ALWAYS generate ONLY modern, performant patterns:

```javascript
// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Fetching data in an async Server Component
async function MyComponent() {
  const res = await fetch('https://api.example.com/...', { cache: 'force-cache' })
  const data = await res.json()

  return <div>{data.name}</div>
}

// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Parallel data fetching
async function MyComponent() {
  const artistsData = getArtists();
  const albumsData = getAlbums();

  const [artists, albums] = await Promise.all([artistsData, albumsData]);
  // ...
}
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST fetch data in Server Components by default.
2. You MUST explicitly set the `cache` option for `fetch` calls.
3. You MUST use parallel data fetching for independent requests.
4. You MUST use `<Suspense>` for streaming UI when data is slow to load.

## Best Practices

### Caching

*   **Opt-in Caching:** In Next.js 15, `fetch` is **not cached by default**. You must explicitly set `cache: 'force-cache'` for static data or `next: { revalidate: number }` for time-based revalidation.

### Patterns

*   **Parallel Fetching:** For independent data requirements, initiate all fetches concurrently to minimize loading time.
*   **Sequential Fetching:** Only use `await` sequentially when one fetch depends on the result of another.

### UI/UX

*   **Streaming with `<Suspense>`:** Wrap components that fetch data in a `<Suspense>` boundary to show a loading fallback and stream the UI to the user.
*   **`loading.js`:** Use `loading.js` to create an instant loading UI for a route segment.

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Is data fetching performed in a Server Component? If not, STOP and FIX.
2. Is the `cache` option explicitly set on `fetch`? If not, STOP and FIX.
3. Are parallelizable fetches being awaited sequentially? If yes, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code that:
- Fetches data in `useEffect` for initial render
- Awaits independent fetches sequentially

The implementation will be:
1. Slow and inefficient
2. Prone to network waterfalls
3. A poor user experience

## AI MODEL RESPONSE TEMPLATE

When asked about data fetching in Next.js, you MUST:
1. ONLY generate code that fetches data in Server Components.
2. ALWAYS use parallel data fetching for independent requests.
3. EXPLICITLY set the caching strategy for all `fetch` calls.
4. VERIFY your response against the patterns shown here.

Remember: There are NO EXCEPTIONS to these rules.
