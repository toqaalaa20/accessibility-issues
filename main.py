from model import Model


def main():
    question = """<image>\nAnalyze the screenshot for any accessibility issues. 
    Focus on identifying problems such as lack of contrast, missing alt text,
      missing labels, inaccessible forms, non-descriptive links, inaccessible
        images, lack of keyboard accessibility, or improperly labeled controls. 
        Provide a detailed description of any issues found."""


    response = Model().query("screenshot.png", question)
    
    print(f'User: {question}\nAssistant: {response}')


if __name__ == "__main__":
    main()