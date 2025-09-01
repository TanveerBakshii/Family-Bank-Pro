"""
Family Bank Pro - Skeleton Application

This module provides basic data structures and functions for managing a family's
financial and estate records. It includes simple in-memory representations for
family members, assets, and important documents. You can extend these functions
with persistent storage, user authentication, and UI components to build a
production-ready family vault.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class FamilyMember:
    """Data class representing a family member."""
    name: str
    relation: str
    contact_info: str

@dataclass
class Asset:
    """Data class representing a financial or estate asset."""
    asset_type: str
    value: float
    owner: str
    description: str

@dataclass
class Document:
    """Data class representing an important document such as a will or ID."""
    doc_type: str
    file_path: str
    description: str

def add_family_member(name: str, relation: str, contact_info: str) -> FamilyMember:
    """Create a new family member record.

    Args:
        name: Full name of the family member.
        relation: The member's relation to the family head (e.g., 'Father', 'Daughter').
        contact_info: Contact information such as email or phone number.

    Returns:
        A FamilyMember instance representing the new member.
    """
    member = FamilyMember(name=name, relation=relation, contact_info=contact_info)
    print(f"Added family member: {member}")
    return member

def add_asset(asset_type: str, value: float, owner: str, description: str) -> Asset:
    """Create a new asset record.

    Args:
        asset_type: Type of asset (e.g., 'Property', 'Bank Account').
        value: Monetary value of the asset.
        owner: Name of the asset owner.
        description: Additional description or notes about the asset.

    Returns:
        An Asset instance representing the new asset.
    """
    asset = Asset(asset_type=asset_type, value=value, owner=owner, description=description)
    print(f"Added asset: {asset}")
    return asset

def add_document(doc_type: str, file_path: str, description: str) -> Document:
    """Create a new document record.

    Args:
        doc_type: Type of the document (e.g., 'Will', 'Property Deed').
        file_path: File path or URL pointing to the document.
        description: Description or notes about the document.

    Returns:
        A Document instance representing the new document.
    """
    document = Document(doc_type=doc_type, file_path=file_path, description=description)
    print(f"Added document: {document}")
    return document

def generate_summary(members: List[FamilyMember], assets: List[Asset], documents: List[Document]) -> None:
    """Generate a simple summary report of all records.

    Args:
        members: A list of FamilyMember objects.
        assets: A list of Asset objects.
        documents: A list of Document objects.

    Returns:
        None. Prints the summary to stdout.
    """
    print("\nFamily Members:")
    for member in members:
        print(f" - {member.name} ({member.relation}) | Contact: {member.contact_info}")

    print("\nAssets:")
    for asset in assets:
        print(f" - {asset.asset_type} owned by {asset.owner} | Value: {asset.value} | Description: {asset.description}")

    print("\nDocuments:")
    for doc in documents:
        print(f" - {doc.doc_type} | File: {doc.file_path} | Description: {doc.description}")

def main() -> None:
    """Demonstrate basic usage of the Family Bank Pro skeleton."""
    members: List[FamilyMember] = []
    assets: List[Asset] = []
    documents: List[Document] = []

    # Sample data creation
    members.append(add_family_member("Tanveer Bakshi", "Self", "tanveer@example.com"))
    members.append(add_family_member("Jane Doe", "Spouse", "jane@example.com"))

    assets.append(add_asset("Property", 500000.0, "Tanveer Bakshi", "Apartment in Bengaluru"))
    assets.append(add_asset("Bank Account", 20000.0, "Jane Doe", "Savings account"))

    documents.append(add_document("Will", "/path/to/will.pdf", "Last will and testament"))
    documents.append(add_document("Aadhar", "/path/to/aadhar.pdf", "National ID"))

    # Generate a summary report
    generate_summary(members, assets, documents)

if __name__ == "__main__":
    main()
