from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def gen_pet_name(animal_type, pet_color):

    llm = OllamaLLM(model = "llama3.2", temperature = 0.7)
    prompt_template_name = PromptTemplate(
        input_variables = ['animal_type', 'pet_color'],
        template = "I have a {animal_type} pet of {pet_color} color and I want a cool name for it. Suggest me five cool names for my pet."
    )

    name_chain = LLMChain(llm = llm, prompt = prompt_template_name, output_key = "pet_names")

    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})
    return response
 
if __name__ == "__main__":
    print(gen_pet_name("cat", "orange"))
