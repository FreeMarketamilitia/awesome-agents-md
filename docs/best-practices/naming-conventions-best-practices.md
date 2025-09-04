# Naming Conventions Best Practices

## Overview

Consistent naming conventions are crucial for code readability, maintainability, and collaboration in software development. This guide provides comprehensive best practices for naming variables, functions, classes, files, and other code elements across different programming languages.

## General Principles

### 1. Use Descriptive, Meaningful Names
```javascript
// Good: Clear intent
userProfileData
calculateTotalPrice()
isAuthenticated()

// Bad: Unclear/vague
data
calc()
flag()
```

### 2. Follow Language-Specific Conventions
Each programming language has established naming conventions that should be respected.

### 3. Be Consistent
Apply the same naming rules throughout your project or codebase.

### 4. Avoid Abbreviations (Unless Widely Known)
Use full words when possible:
```javascript
// Good
customerEmailAddress
maximumRetryCount

// Bad
custEmailAddr
maxRetryCnt
```

## Programming Language Conventions

### JavaScript/TypeScript

#### Variables and Constants
- **camelCase** for variables and functions
- **UPPER_SNAKE_CASE** for constants
- **PascalCase** for classes and constructors

```javascript
// Variables
let userName = "john_doe";
const MAX_RETRY_ATTEMPTS = 3;

// Functions
function calculateTotalPrice() { }

// Classes
class UserProfile {
  constructor(userName) {
    this.userName = userName;
  }
}
```

#### File Naming
- Use lowercase with hyphens for file names
- Prefer `.js` for JavaScript, `.ts` for TypeScript

```
user-profile.js
data-validation.ts
auth-service.js
```

### Python

#### Variables and Functions
- **snake_case** for variables, functions, and methods
- **UPPER_SNAKE_CASE** for constants
- **PascalCase** for classes

```python
# Variables
user_name = "john_doe"
MAX_RETRY_ATTEMPTS = 3

# Functions
def calculate_total_price():
    pass

# Classes
class UserProfile:
    def __init__(self, user_name):
        self.user_name = user_name
```

#### Module and Package Names
- Use lowercase with underscores
- Avoid dashes and uppercase letters

```
user_profile.py
data_validation.py
auth_service/
```

### Java

#### Variables and Methods
- **camelCase** for variables and methods
- **UPPER_SNAKE_CASE** for constants
- **PascalCase** for classes and interfaces

```java
// Variables
String userName = "john_doe";
final int MAX_RETRY_ATTEMPTS = 3;

// Methods
public void calculateTotalPrice() { }

// Classes
public class UserProfile {
    private String userName;

    public UserProfile(String userName) {
        this.userName = userName;
    }
}
```

#### Package Names
- Use lowercase with reverse domain notation
- Start with your organization's domain

```
com.company.project.userprofile
com.myapp.service.auth
```

### Go

#### Variables and Functions
- **camelCase** for most identifiers
- **PascalCase** for exported identifiers
- **snake_case** rarely used

```go
// Private (lowercase)
userName := "john_doe"
maxRetryAttempts := 3

// Exported (uppercase)
func CalculateTotalPrice() {
    // Implementation
}

type UserProfile struct {
    UserName string
}
```

### C#

#### Variables and Methods
- **camelCase** for private fields, parameters, local variables
- **PascalCase** for public properties, methods, classes, structs
- **UPPER_SNAKE_CASE** or PascalCase for constants

```csharp
// Private fields
private string userName;

// Public properties
public string UserName { get; set; }

// Methods
public void CalculateTotalPrice() { }

// Classes
public class UserProfile {
    // Implementation
}
```

## Database Conventions

### Table Names
- **snake_case** or **PascalCase**
- Use plural nouns for table names
- Avoid reserved words

```sql
-- Good
user_profiles
order_items

-- Bad
userprofile
orderitems
user
```

### Column Names
- **snake_case** for most databases
- Use clear, descriptive names
- Add table prefix if needed to avoid conflicts

```sql
user_name
email_address
created_at
updated_timestamp
```

### Primary Keys
- Use `id` or `table_name_id`
- Prefer auto-incrementing integers

```sql
user_id (primary key)
profile_id (foreign key)
```

## API Conventions

### RESTful Endpoints
Use lowercase with hyphens:
```
/api/users
/api/users/{id}
/api/users/{id}/profile
```

### Query Parameters
Use camelCase:
```
/api/users?firstName=john&lastName=doe
```

### HTTP Methods
Follow REST conventions:
- `GET /users` - Retrieve users
- `POST /users` - Create user
- `PUT /users/{id}` - Update user
- `DELETE /users/{id}` - Delete user

## Version Control

### Branch Naming
Use descriptive prefixes:
```
feature/user-authentication
bugfix/login-validation
hotfix/security-patch
release/v1.2.0
```

### Commit Messages
Follow conventional commits format:
```
feat: add user authentication
fix: resolve login validation bug
docs: update API documentation
```

## Configuration Files

### Environment Variables
- **UPPER_SNAKE_CASE**
- Use descriptive names with prefixes

```
DATABASE_URL
REDIS_HOST
API_SECRET_KEY
MAX_CONNECTION_POOL_SIZE
```

### Configuration Files
Use appropriate extensions and naming:
```
.dockerignore
.gitignore
.eslintrc.js
.prettierrc.json
babel.config.js
```

## Testing Conventions

### Test Files
- Mirror source file structure
- Use descriptive suffixes

```
user-service.js → user-service.test.js
user.service.ts → user.service.spec.ts
UserService.java → UserServiceTest.java
```

### Test Function Names
- Describe behavior clearly
- Use descriptive words

```javascript
// Good
describe('calculateTotalPrice', () => {
  test('should calculate total with tax', () => {
    // Implementation
  });

  test('should handle zero items', () => {
    // Implementation
  });
});
```

## Best Practices Summary

### 1. **Prioritize Readability**
Names should be self-documenting and easy to understand.

### 2. **Follow Established Conventions**
Don't reinvent naming rules - use language and framework standards.

### 3. **Be Consistent Across Your Team**
Establish team-specific guidelines for consistency.

### 4. **Use Tools for Enforcement**
Use linters, formatters, and code review guidelines to maintain consistency.

### 5. **Document Your Conventions**
Keep your naming conventions documented and accessible to team members.

### 6. **Refactor When Needed**
Don't be afraid to rename when better names emerge.

## Common Pitfalls to Avoid

- **Using single letters**: Except for loop variables or well-known conventions
- **Inconsistent capitalization**: Stick to one convention per language
- **Meaningless names**: Avoid `variable1`, `function_A`
- **Over-abbreviation**: Use `configuration` instead of `cfg`
- **Mixed conventions**: Don't mix camelCase and snake_case in same codebase

## Tools for Enforcement

### Linters and Formatters
- ESLint + Prettier (JavaScript/TypeScript)
- Black + isort (Python)
- Spotless (Java)
- gofmt (Go)
- StyleCop (C#)

### Editor Extensions
- Language-specific extensions
- Code spell checkers
- Naming convention helpers

Following these best practices will make your codebase more maintainable, readable, and professional.
