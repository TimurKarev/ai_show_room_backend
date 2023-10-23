from rest_framework.views import APIView
from rest_framework.response import Response
from firebase_admin import initialize_app, storage
from ai_lib import files, qdrant_db, embeddings, retriver
from ai_lib.variables import EmbeddingTypeSized

class AskQuestion(APIView):
    embedding_type = EmbeddingTypeSized.OPEN_AI
    def get(self, request):
        print(request.query_params.get('collection_name'))
        collection_name = request.query_params.get("collection_name")
        user_id = request.query_params.get("user_id")
        query = request.query_params.get("query")
        if collection_name is None:
            return Response("Missing collection_name parameter", 400)
        if user_id is None:
            return Response("Missing user_id parameter", 400)
        if query is None:
            return Response("Missing query parameter", 400)

        embedding = embeddings.get_embedding(type=self.embedding_type)
        qdrant_db.get_or_create_collection(name=collection_name,
                                           collection_size=self.embedding_type
                                           )
        context_vector_store = qdrant_db.get_vector_store(
            embeddings=embedding,
            collection_name=collection_name,
        )

        # rag_chain = retriver.get_rag_chain(
        #     context_vector_store
        # )
        #
        # response = rag_chain.invoke(query)

        response = retriver.get_retriever_chain(context_vector_store).run(query)

        return Response(response)
