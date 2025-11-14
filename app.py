import gradio as gr

def greet(name):
    return f"Hey {name}!"

demo = gr.Interface(greet, "text", "text")
demo.launch()
