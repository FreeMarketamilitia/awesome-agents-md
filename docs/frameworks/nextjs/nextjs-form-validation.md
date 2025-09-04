---
description: Guidelines for Form Validation in Next.js 15+
author: Gemini
version: 1.0
tags: ["nextjs", "form-validation", "server-actions", "zod", "useActionState"]
globs: ["**/app/**/*.tsx", "**/app/**/*.jsx"]
---

# Next.js 15+ Form Validation Best Practices

## Overview of Form Validation

Effective form validation in Next.js 15+ leverages React Server Actions and the `useActionState` hook, combined with a schema validation library like Zod. This approach ensures both client-side responsiveness and crucial server-side data integrity.

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns:

```javascript
// ❌ NEVER GENERATE THIS CODE - IT IS INSECURE
// Relying solely on client-side validation
'use client'
function MyForm() {
  const handleSubmit = (e) => {
    e.preventDefault()
    // Only client-side validation here
    if (e.target.email.value === '') {
      alert('Email is required')
      return
    }
    // ... submit form
  }
  // ...
}

// ❌ NEVER GENERATE THIS CODE - IT IS INEFFICIENT
// Manually handling form state and errors without useActionState
'use client'
import { useState } from 'react'

function MyForm() {
  const [email, setEmail] = useState('')
  const [errors, setErrors] = useState({})

  const handleSubmit = async (e) => {
    e.preventDefault()
    // Manual validation and error setting
    if (email === '') {
      setErrors({ email: 'Email is required' })
      return
    }
    // ...
  }
  // ...
}
```

Instead, you MUST ALWAYS generate ONLY modern, secure patterns:

```javascript
// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Using Zod for schema definition (shared between client and server)
// lib/schemas.ts
import { z } from 'zod'

export const contactFormSchema = z.object({
  email: z.string().email({ message: "Invalid email address" }),
  message: z.string().min(10, { message: "Message must be at least 10 characters" }),
});

// ✅ ALWAYS GENERATE THIS EXACT PATTERN
// Server Action with Zod validation and useActionState
'use server'
import { useActionState } from 'react'
import { contactFormSchema } from '@/lib/schemas'

async function submitContactForm(prevState, formData) {
  const parsed = contactFormSchema.safeParse({
    email: formData.get('email'),
    message: formData.get('message'),
  })

  if (!parsed.success) {
    return { errors: parsed.error.flatten().fieldErrors }
  }

  // ... process valid data
  return { message: 'Form submitted successfully!' }
}

function ContactForm() {
  const [state, formAction] = useActionState(submitContactForm, {})

  return (
    <form action={formAction}>
      <input type="email" name="email" />
      {state.errors?.email && <p>{state.errors.email}</p>}
      <textarea name="message"></textarea>
      {state.errors?.message && <p>{state.errors.message}</p>}
      <button type="submit">Submit</button>
      {state.message && <p>{state.message}</p>}
    </form>
  )
}
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST implement validation on both the client and server.
2. You MUST use React Server Actions for form submissions.
3. You MUST use the `useActionState` hook to manage form state and display errors.
4. You MUST use a schema validation library like Zod for defining validation rules.

## Best Practices

### Dual Validation

*   **Client-side:** Provides immediate feedback to the user for a better UX.
*   **Server-side:** Crucial for security and data integrity, as client-side checks can be bypassed.

### Server Actions & `useActionState`

*   **Server Actions:** Handle form submissions directly on the server, enabling direct database interaction.
*   **`useActionState`:** Simplifies managing form states, including error messages and pending states, based on the server action's outcome.

### Schema Validation with Zod

*   **Single Source of Truth:** Define your validation schema using Zod in a shared file. This schema can then be used for validation on both the client and server, ensuring consistency and reducing duplication.

### Displaying Errors

*   **Conditional Rendering:** Use the `state` object returned by `useActionState` to conditionally render error messages next to the relevant form fields.

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Is validation performed on both client and server? If not, STOP and FIX.
2. Are Server Actions used for form submission? If not, STOP and FIX.
3. Is `useActionState` used for form state management? If not, STOP and FIX.
4. Is Zod (or a similar schema validation library) used? If not, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code that:
- Relies solely on client-side validation
- Does not use Server Actions for form submission
- Manually handles form state and errors

The implementation will be:
1. Insecure and vulnerable to invalid data
2. Less performant due to unnecessary client-server roundtrips
3. More complex and harder to maintain

## AI MODEL RESPONSE TEMPLATE

When asked about form validation in Next.js, you MUST:
1. ONLY generate code that uses Server Actions and `useActionState`.
2. ALWAYS include dual (client-side and server-side) validation.
3. RECOMMEND using Zod for schema definition.
4. VERIFY your response against the patterns shown here.

Remember: There are NO EXCEPTIONS to these rules.
