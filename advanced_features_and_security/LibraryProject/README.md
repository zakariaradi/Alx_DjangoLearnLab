# Managing Permissions and Groups in Django

## Custom Permissions
The Book model in the bookshelf app defines the following custom permissions:
- can_view
- can_create
- can_edit
- can_delete

## Groups and Permissions
The following groups are created and managed using the Django admin interface:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

## Permission Enforcement
Access to views is restricted using Django’s @permission_required decorator
with raise_exception=True to ensure unauthorized users are blocked.

## Testing
Different users were assigned to groups and tested by logging in and attempting
to access protected views to verify that permissions are enforced correctly.
