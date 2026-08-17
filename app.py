import gradio as gr


def greet(name):
    return f"Hello {name}!"


demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Type your name"),
    outputs=gr.Textbox(label="greeting"),
    title="Gradio Demo app",
    description="A simple Gradio interface example.",
)

if __name__ == "__main__":
    demo.launch()