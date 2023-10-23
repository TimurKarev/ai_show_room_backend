from langchain.embeddings import HuggingFaceInstructEmbeddings, OpenAIEmbeddings

from .variables import EmbeddingTypeSized


def get_embedding(type: EmbeddingTypeSized):
    if (type == EmbeddingTypeSized.HUGGING_FACE_INSTRUCTOR):
        return HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")

    if (type == EmbeddingTypeSized.OPEN_AI):
        return OpenAIEmbeddings()
