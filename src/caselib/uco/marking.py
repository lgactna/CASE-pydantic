"""
Auto-generated classes from the SHACL graph in marking.ttl.

This file was generated using the `case_models.py` script.
"""

from caselib.uco import core


class MarkingModel(core.UcoInherentCharacterizationThing):
    """
    A marking model is a grouping of characteristics unique to the expression of
    a particular form of data marking definitions (restrictions, permissions,
    and other guidance for how data can be used and shared).
    """


class LicenseMarking(MarkingModel):
    """
    A license marking is a grouping of characteristics unique to the expression
    of data marking definitions (restrictions, permissions, and other guidance
    for how data can be used and shared) to convey details of license
    restrictions that apply to the data.
    """

    definitionType: str | list[str] | None = []
    license: str


class MarkingDefinition(core.MarkingDefinitionAbstraction):
    """
    A marking definition is a grouping of characteristics unique to the
    expression of a specific data marking conveying restrictions, permissions,
    and other guidance for how marked data can be used and shared.
    """

    definition: MarkingModel | list[MarkingModel] | None = []
    definitionType: str


class ReleaseToMarking(MarkingModel):
    """
    A release-to marking is a grouping of characteristics unique to the
    expression of data marking definitions (restrictions, permissions, and other
    guidance for how data can be used and shared) to convey details of
    authorized persons and/or organizations to which to the associated content
    may be released. The existence of the Release-To marking restricts access to
    ONLY those identities explicitly listed, regardless of whether another data
    marking exists that allows sharing with other members of the community.
    """

    definitionType: str | list[str] | None = []
    authorizedIdentities: str | list[str] = []


class StatementMarking(MarkingModel):
    """
    A statement marking is a grouping of characteristics unique to the
    expression of data marking definitions (restrictions, permissions, and other
    guidance for how data can be used and shared) to convey details of a textual
    marking statement, (e.g., copyright) whose semantic meaning should apply to
    the associated content. Statement markings are generally not
    machine-readable. An example of this would be a simple marking to apply
    copyright information, such as 'Copyright 2014 Acme Inc.'.
    """

    definitionType: str | list[str] | None = []
    statement: str


class TermsOfUseMarking(MarkingModel):
    """
    A terms of use marking is a grouping of characteristics unique to the
    expression of data marking definitions (restrictions, permissions, and other
    guidance for how data can be used and shared) to convey details of a textual
    statement specifying the Terms of Use (that is, the conditions under which
    the content may be shared, applied, or otherwise used) of the marked
    content. An example of this would be used to communicate a simple statement,
    such as 'Acme Inc. is not responsible for the content of this file'.
    """

    definitionType: str | list[str] | None = []
    termsOfUse: str


class GranularMarking(core.UcoInherentCharacterizationThing):
    """
    A granular marking is a grouping of characteristics unique to specification
    of marking definitions (restrictions, permissions, and other guidance for
    how data can be used and shared) that apply to particular portions of a
    particular UCO object.
    """

    marking_: MarkingDefinition | list[MarkingDefinition] | None = []
    contentSelectors: str | list[str] | None = []
