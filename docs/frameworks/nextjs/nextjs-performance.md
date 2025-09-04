---
description: Guidelines for Performance Optimization in Next.js 15+
author: Gemini
version: 1.0
tags: ["nextjs", "performance", "optimization", "core-web-vitals", "caching", "image-optimization"]
globs: ["**/app/**/*.tsx", "**/app/**/*.jsx", "next.config.mjs"]
---

# Next.js 15+ Performance Optimization Best Practices

## Overview of Performance Optimization

Next.js 15 offers powerful features for building high-performance web applications. Optimizing rendering strategies, mastering caching, efficient image handling, and effective code splitting are crucial for achieving excellent Core Web Vitals and a superior user experience.

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns:

```javascript
// ❌ NEVER GENERATE THIS CODE - IT IS INEFFICIENT
// Using standard <img> tags instead of next/image
<img src="/my-image.jpg" alt="My Image" />

// ❌ NEVER GENERATE THIS CODE - IT IS INEFFICIENT
// Client-side rendering for static content
'use client'
import { useEffect, useState } from 'react'

function StaticContent() {
  const [data, setData] = useState(null)
  useEffect(() => {
    // Fetch static data on client
  }, [])
  // ...
}
```

Instead, you MUST ALWAYS generate ONLY modern, performant patterns:

```javascript
// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Using next/image for optimized images
import Image from 'next/image'

<Image
  src="/my-image.jpg"
  alt="A descriptive alt text"
  width={500}
  height={300}
  priority // For above-the-fold images
/>

// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Using Server Components for static content
async function StaticContent() {
  // Data fetched on server
  return <div>Static content here</div>
}
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use the `<Image>` component from `next/image` for all images.
2. You MUST default to Server Components for rendering and data fetching.
3. You MUST implement explicit caching strategies for `fetch` requests.
4. You MUST use dynamic imports (`next/dynamic`) for non-critical components.

## Best Practices

### Rendering Strategies

*   **React Server Components (RSC):** Default to RSC to minimize client-side JavaScript and improve initial load times.
*   **Static Site Generation (SSG):** Use for content that doesn't change frequently, pre-rendering pages at build time.
*   **Incremental Static Regeneration (ISR):** Combine SSG benefits with dynamic updates for content that changes occasionally.
*   **Server-Side Rendering (SSR):** Use for highly dynamic, user-specific content. Leverage Partial Pre-rendering (PPR) for mixed content.

### Caching

*   **Explicit `fetch` Caching:** Next.js 15 `fetch` requests are `no-store` by default. Explicitly use `cache: 'force-cache'` or `next: { revalidate: number }`.
*   **`use cache` Directive:** For granular control over caching functions, components, or routes.
*   **Tag-based Revalidation:** Use `revalidateTag` for on-demand cache invalidation.

### Image Optimization

*   **`next/image` Component:** Automatically optimizes images (sizing, formats, lazy loading, CLS prevention).
*   **`priority` Prop:** Use for above-the-fold images to improve LCP.

### Code Splitting & Bundle Size

*   **Automatic Code Splitting:** Next.js automatically splits code by page.
*   **Dynamic Imports (`next/dynamic`):** Lazy-load components or libraries that are not critical for initial render.
*   **Minimize Client JavaScript:** Keep `"use client"` components small and push logic to Server Components.

### Other Optimizations

*   **Font Optimization:** Use `next/font` to optimize font loading.
*   **Streaming with Suspense:** Improve perceived performance by streaming UI with `<Suspense>` for slower data fetches.

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are images optimized with `next/image`? If not, STOP and FIX.
2. Is the default rendering strategy Server Components? If not, STOP and FIX.
3. Are caching strategies explicitly defined? If not, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code that:
- Uses unoptimized images
- Relies on inefficient rendering strategies
- Lacks explicit caching controls

The application will have:
1. Slow loading times
2. Poor Core Web Vitals scores
3. A suboptimal user experience

## AI MODEL RESPONSE TEMPLATE

When asked about performance optimization in Next.js, you MUST:
1. ONLY generate code that adheres to the best practices for Next.js 15+.
2. ALWAYS prioritize Server Components and explicit caching.
3. VERIFY your response against the patterns shown here.

Remember: There are NO EXCEPTIONS to these rules.
