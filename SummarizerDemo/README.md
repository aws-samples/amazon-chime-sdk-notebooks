## Call Summarizer 

We have provided a notebook that walks the user through (1) loading a transcript, (2) preparing it as a summarization task prompt for a Large Language Model, (3) submits the prompt to the model, and (4) saves the output as a summary. 

Several LLM options are available to users. We used Cohere in the notebook because it is available as a [SageMaker Model Package](https://aws.amazon.com/blogs/machine-learning/cohere-brings-language-ai-to-amazon-sagemaker/). To gain access to the LLM used in this blog, please [Subscribe to Foundation Models](https://aws.amazon.com/sagemaker/jumpstart/getting-started/); in the AWS console, go to SageMaker and choose Jumpstart -> Foundation Models on the left toolbar. You will either have access and see the options, or you will need to Request Access and wait 24 hours. Once you have access to Foundation Models, subscribe to [cohere-gpt-medium](https://aws.amazon.com/marketplace/pp/prodview-6dmzzso5vu5my); this provides access to the LLM used here.

The Notebook allows users to test access to the LLM and engineer prompts specific to their problem. Start a Notebook Instance of size ml.t3.medium, and navigate to Jupyter Lab on your notebook instance once available. Clone this repository using the Git dropdown menu in JupyterLab.


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

