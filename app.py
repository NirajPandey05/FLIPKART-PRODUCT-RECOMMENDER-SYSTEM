from flask import Flask, request, Response, render_template
from prometheus_client import Counter, generate_latest

from flipkart.data_ingestion import DataIngestor
from flipkart.rag_chain import RAGChainBuilder

from dotenv import load_dotenv
load_dotenv()

REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests")
def create_app():
    app = Flask(__name__)

    vector_store = DataIngestor().ingest(True) #load_existing_data=True
    # Initialize Data Ingestion and RAG Chain Builder

    rag_chain = RAGChainBuilder(vector_store).build_chain()

    @app.route('/')
    def index():
        REQUEST_COUNT.inc()
        return render_template('index.html')

    @app.route('/get', methods=['POST'])
    def get_response():
        user_input = request.form['msg']
        response = rag_chain.invoke(
            {"input" : user_input},
            config={"configurable": {"session_id": "user-session"}}
        )["answer"]

        return response
    
    @app.route('/metrics') 
    def metrics():
        return Response(generate_latest(), mimetype="text/plain")

    return app


    

    

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)