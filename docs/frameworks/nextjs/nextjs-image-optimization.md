---
description: Guidelines for Image Optimization in Next.js 15+
author: Gemini
version: 1.0
tags: ["nextjs", "image-optimization", "performance", "next-image", "core-web-vitals"]
globs: ["**/app/**/*.tsx", "**/app/**/*.jsx", "next.config.mjs"]
---

# Next.js 15+ Image Optimization Best Practices

## Overview of Image Optimization

Next.js provides a powerful, built-in `<Image>` component that automates many image optimization best practices. Using this component correctly is crucial for achieving good performance and high Core Web Vitals scores.

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns:

```javascript
// ❌ NEVER GENERATE THIS CODE - IT IS NOT OPTIMIZED
// Using the standard <img> tag
<img src="/my-image.jpg" alt="My Image" />

// ❌ NEVER GENERATE THIS CODE - IT CAUSES LAYOUT SHIFT
// Using next/image without width and height for remote images
import Image from 'next/image'
<Image src="https://example.com/image.jpg" alt="My Image" />
```

Instead, you MUST ALWAYS generate ONLY modern, performant patterns:

```javascript
// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Using the next/image component with required props
import Image from 'next/image'

<Image
  src="/my-image.jpg" // or a statically imported image object
  alt="A descriptive alt text"
  width={500}
  height={300}
/>

// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Prioritizing above-the-fold images
<Image
  src="/hero-image.jpg"
  alt="A descriptive alt text for the hero image"
  width={1200}
  height={400}
  priority
/>
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use the `<Image>` component from `next/image` instead of the `<img>` tag.
2. You MUST provide `width` and `height` props for all remote images.
3. You MUST use the `priority` prop for above-the-fold images.
4. You MUST configure `remotePatterns` in `next.config.mjs` for remote images.

## Best Practices

### Essential Props

*   **`width` and `height`:** Always provide these for remote images to prevent Cumulative Layout Shift (CLS).
*   **`alt`:** Provide a descriptive alt text for accessibility.
*   **`priority`:** Use for images that are visible in the initial viewport (e.g., hero images) to improve Largest Contentful Paint (LCP).

### Responsive Images

*   **`sizes`:** Use the `sizes` prop to specify how the image will be displayed at different breakpoints. This is crucial for responsive layouts.
*   **`fill`:** Use the `fill` prop when you don't know the image dimensions and want it to fill its parent container. The parent must have `position: relative`.

### Remote Images

*   **`remotePatterns`:** Configure allowed hostnames in `next.config.mjs` to securely use remote images.

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you using the `<Image>` component? If not, STOP and FIX.
2. Do remote images have `width` and `height` props? If not, STOP and FIX.
3. Is the `priority` prop used for LCP-critical images? If not, consider adding it.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code that:
- Uses the `<img>` tag
- Omits `width` and `height` for remote images

The implementation will have:
1. Poor performance
2. High CLS, which hurts SEO and user experience
3. Larger than necessary image downloads

## AI MODEL RESPONSE TEMPLATE

When asked about images in Next.js, you MUST:
1. ONLY generate code that uses the `<Image>` component.
2. ALWAYS include `width`, `height`, and `alt` props.
3. RECOMMEND using the `priority` prop for above-the-fold images.
4. VERIFY your response against the patterns shown here.

Remember: There are NO EXCEPTIONS to these rules.
