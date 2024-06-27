import gradio as gr
from register import sign_up, sign_in
from bank import banking_service

def main():
    with gr.Blocks() as demo:
        with gr.Tab("Sign Up"):
            username = gr.Textbox(label="Username")
            password = gr.Textbox(label="Password", type="password")
            name = gr.Textbox(label="Name")
            age = gr.Number(label="Age")
            city = gr.Textbox(label="City")
            sign_up_btn = gr.Button("Sign Up")
            sign_up_output = gr.Textbox()
            sign_up_btn.click(sign_up, inputs=[username, password, name, age, city], outputs=sign_up_output)

        with gr.Tab("Sign In"):
            username = gr.Textbox(label="Username")
            password = gr.Textbox(label="Password", type="password")
            sign_in_btn = gr.Button("Sign In")
            sign_in_output = gr.Textbox()
            account_number_output = gr.Textbox()
            sign_in_btn.click(sign_in, inputs=[username, password], outputs=[sign_in_output, account_number_output])

        with gr.Tab("Banking Services"):
            username = gr.Textbox(label="Username")
            account_number = gr.Textbox(label="Account Number")
            service = gr.Radio(choices=["Balance Enquiry", "Cash Deposit", "Cash Withdraw", "Fund Transfer"], label="Service")
            amount = gr.Number(label="Amount", value=0)
            receiver_account = gr.Textbox(label="Receiver Account Number", value="")
            banking_btn = gr.Button("Submit")
            banking_output = gr.Textbox()
            banking_btn.click(banking_service, inputs=[username, account_number, service, amount, receiver_account], outputs=banking_output)

    demo.launch()

if __name__ == "__main__":
    main()
