from flask import Blueprint, request
from application.text_checker.quick_solution_fuzzywuzzy import basic_checker, checker

text_bp = Blueprint("text_bp", __name__, template_folder="templates")


@text_bp.route("/search1", methods=["GET", "POST"])
def check_text():
    if not request.form.get("user_input"):
        if not request.args.get("user_input"):
            return "input was false"
        else:
            input = request.args.get("user_input")
            if isinstance(input, list):
                output = []
                for item in input:
                    output.append(checker(item))
                return {"output": output}
            elif isinstance(input, str):
                output = checker(input)
                return {"output": output}
            else:
                return {"output": None}
    else:
        response = checker(request.form.get("user_input"))
        return response


@text_bp.route("/search2/<user_input>", methods=["GET", "POST"])
def check_text2(user_input):
    if user_input:
        response = checker(user_input)
        return response
    return "didnt work"


@text_bp.route("/search_json", methods=["GET", "POST"])
def check_text3():
    if request.get_json():
        input = request.get_json()
        sentences = input["sentences"]

        output = []
        for item in sentences:
            output.append(checker(item))

        return "it is not none" \
               "with sentences {}" \
               "and output {}".format(sentences, output)

    return "didnt work"