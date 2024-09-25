import google.generativeai as genai
import gradio as gr

def carbonFootPrintAI(monthly_oil_bill: int,
                      monthly_gas_bill: int,
                      monthly_electricity_bill: int,
                      total_yearly_mileage_on_car: int,
                      number_of_flights_in_past_year_less_or_equal_4hours: int,
                      number_of_flights_in_past_year_more_or_equal_4hours: int,
                      recycle_newspaper=False,
                      recycle_aluminium_and_tin=False):

    genai.configure(api_key="GEMINI_API_KEY")

    model = genai.GenerativeModel("gemini-pro")

    # Calculate base values
    e_bill = monthly_electricity_bill * 105
    o_bill = monthly_oil_bill * 113
    g_bill = monthly_gas_bill * 105
    y_mileage = total_yearly_mileage_on_car * 0.79
    f_less_than_4hours = number_of_flights_in_past_year_less_or_equal_4hours * 1100
    f_more_than_4hours = number_of_flights_in_past_year_more_or_equal_4hours * 4400

    # Total footprint without recycling adjustments
    total_footprint = e_bill + o_bill + g_bill + y_mileage + f_less_than_4hours + f_more_than_4hours

    # Add penalties if not recycling
    if not recycle_newspaper:
        total_footprint += 184
    if not recycle_aluminium_and_tin:
        total_footprint += 166

    if total_footprint < 6000:
        prompt1 = """
        commend for excellent work keeping total carbon footprint down at {} and recommend suggestions to keep it that way.
        Give suggestions regarding monthly electricity bill, monthly gas bill, monthly oil bill, total yearly mileage on car, number of flights
        less than or equal to 4 hours, and number of flights more than or equal to 4 hours.
        """.format(total_footprint)
        response1 = model.generate_content(prompt1)
        return [total_footprint, response1.text]

    elif total_footprint > 6000 and total_footprint < 15999:
        prompt2 = """
        commend for keeping total carbon footprint down at {} and recommend practical suggestions to bring it down further.
        Give suggestions regarding monthly electricity bill, monthly gas bill, monthly oil bill, total yearly mileage on car, number of flights
        less than or equal to 4 hours, and number of flights more than or equal to 4 hours.
        """.format(total_footprint)
        response2 = model.generate_content(prompt2)
        return [total_footprint, response2.text]

    elif total_footprint > 16000 and total_footprint < 22000:
        prompt3 = """
        commend for keeping total carbon footprint at an average of {} and recommend useful suggestions to make sure it doesn't get higher than that.
        Give suggestions regarding monthly electricity bill, monthly gas bill, monthly oil bill, total yearly mileage on car, number of flights
        less than or equal to 4 hours, and number of flights more than or equal to 4 hours.
        """.format(total_footprint)
        response3 = model.generate_content(prompt3)
        return [total_footprint, response3.text]

    elif total_footprint > 22000:
        prompt4 = """
        urgently recommend drastic and practical measures to bring carbon footprint down from {}. Give suggestions regarding monthly electricity bill, monthly gas bill, monthly oil bill, total yearly mileage on car, number of flights
        less than or equal to 4 hours, and number of flights more than or equal to 4 hours.
        """.format(total_footprint)
        response4 = model.generate_content(prompt4)
        return [total_footprint, response4.text]


css = """
.app {
    border-width: 3px;
    border-color: forestgreen;
}
"""
# Gradio Interface
app = gr.Interface(
    fn=carbonFootPrintAI,
    inputs=[
        gr.Number(label="Monthly Gas Bill", elem_classes="app"),
        gr.Number(label="Monthly Oil Bill", elem_classes="app"),
        gr.Number(label="Monthly Electricity Bill", elem_classes="app"),
        gr.Slider(label="Total Yearly Mileage on Car", value = 0, minimum = 0, maximum = 50000, step = 1, elem_classes="app"),
        gr.Slider(label="Number of Flights Less Than or Equal to 4 Hours", value = 0, minimum = 0, maximum = 100, step = 1, elem_classes="app"),
        gr.Slider(label="Number of Flights More Than or Equal to 4 Hours", value = 0, minimum = 0, maximum = 100, step = 1, elem_classes="app"),
        gr.Checkbox(label="Do You Recycle Newspaper?", elem_classes="app"),
        gr.Checkbox(label="Do You Recycle Aluminium and Tin?", elem_classes="app")
    ],
    outputs=[
        gr.Number(label="Total Carbon Footprint", elem_classes="app"),
        gr.Markdown(label="Recommendation", elem_classes="app")
    ],
    theme = gr.themes.Soft(),
    title = "&#127757; &#127807; Carbon Footprint Calculator &#127757; &#127807;"
)

app.launch()
