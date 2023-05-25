from SoftLayer.sltypes.Entity import Entity

class Container_KnowledgeLayer_QuestionAnswer(Entity):
    """SoftLayer_Container_KnowledgeLayer_QuestionAnswer models a single question and answer pair from SoftLayer's
KnowledgeLayer knowledge base. SoftLayer's backend network interfaces with the KnowledgeLayer to recommend
helpful articles when support tickets are created."""
    answer: str
    link: str
    question: str
