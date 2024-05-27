from sqlalchemy.orm import Session

from src.auth.schemas import User
from src.organization import models, schemas


def create_organization(db: Session, user: User, organization: schemas.OrganizationCreate):
    """
    Create an organization.

    - Setup a new organization.
    - Create a 'Owner' role for the organization.
    - Setup 'Owner' role permissions for all resources.
    - Create a 'Membership' for the user who created the organization with the 'Owner' role.
    """
    db_organization = models.Organization(slug=organization.slug)
    db_role = models.Role(name="Owner", organization=db_organization)
    # TODO avaliate how to setup permissions for all resources
    resources = ['roles', 'organizations', 'memberships', 'clients', 'sales']
    db_permissions = []
    for resource in resources:
        db_permissions.append(
            models.Permission(resource=resource, role=db_role)
        )
    db_membership = models.Membership(
        user_id=user.id, organization=db_organization, role=db_role
    )
    db.add(db_membership)
    db.add(db_role)
    db.add_all(db_permissions)
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization
