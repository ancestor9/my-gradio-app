import gradio as gr
import spaces

# ZeroGPU 사용 함수 (실제 UI인 Interface의 fn과 연결)
@spaces.GPU
def predict(input_text):
    # GPU 모델 추론 로직 작성 위치
    output = f"Hello {input_text}!"
    return output

# Gradio 인터페이스 구성
demo = gr.Interface(
    fn=predict,  # @spaces.GPU가 적용된 함수를 연결
    inputs=gr.Textbox(label="Type your name ...."),
    outputs=gr.Textbox(label="greeting wwwwwwwww!"),
    title="Gradio Demo app",
    description="A simple Gradio interface example.",
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)