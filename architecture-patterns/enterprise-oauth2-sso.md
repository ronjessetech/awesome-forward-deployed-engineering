# Enterprise OAuth2, OIDC, SAML SSO & Multi-Tenant RBAC

One of the fastest ways to stall an enterprise pilot is failing security review. Forward Deployed Engineers should design **tenant isolation and enterprise identity** cleanly from Day 1.

---

## 1. Core Enterprise Identity Stack
- **OIDC / OAuth2 (`Authorization Code + PKCE`):** Standard for modern identity providers (Okta, Microsoft Entra ID, Google Workspace).
- **SAML 2.0:** Still common in legacy finance, healthcare, and manufacturing enterprises; bridge it cleanly at the auth gateway layer rather than hand-rolling XML parsers inside your app business logic.
- **SCIM Provisioning:** Automated user de-provisioning when an employee leaves the client organization.

---

## 2. JWT & JWKS Verification Checklist
Never trust unverified JWT payloads or hardcode static public keys:
1. Fetch the Identity Provider's **JWKS** (`/.well-known/jwks.json`) and cache keys by `kid` with automatic refresh on unknown key IDs.
2. Validate **`iss`** (issuer matches client IdP), **`aud`** (audience matches your app client ID), and **`exp`** / **`nbf`** timestamps.
3. Extract `tenant_id` (organization claim) from the **verified server-side token**, never from an untrusted HTTP body or query parameter.

---

## 3. Multi-Tenant RBAC Enforcement Pattern

Enforce authorization **at the boundary** before any database read or write:

```python
from fastapi import Depends, HTTPException, status

ROLE_PERMISSIONS = {
    "Admin": {"read:data", "write:data", "manage:connectors", "view:audit"},
    "Operator": {"read:data", "write:data"},
    "Viewer": {"read:data"},
}

def require_permission(permission: str):
    def dependency(current_user: dict = Depends(verify_jwt_token)):
        role = current_user.get("role", "Viewer")
        if permission not in ROLE_PERMISSIONS.get(role, set()):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Missing required permission: {permission}",
            )
        return current_user
    return dependency
```

---

## 4. Zero-Trust Audit Logging
Enterprise security teams almost always require an immutable audit trail answering: **Who accessed or changed what tenant record, when, and from where?**

Log structured JSON audit events (without sensitive PII or tokens) for:
- Login / SSO authentication successes & failures
- Connector credential updates or API key rotations
- Role / permission escalations
- Bulk data exports or AI query invocations
