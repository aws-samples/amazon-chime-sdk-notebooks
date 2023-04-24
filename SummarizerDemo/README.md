## Call Summarization in Amazon Chime SDK Call Analytics using a Large Language Model

### Amazon Chime SDK Call Analytics

The Amazon Chime SDK is a set of composable APIs that enable builders to add communications capabilities to their applications. Amazon Chime SDK offers real-time call analytics to help businesses extract insights from voice conversations. Call summarization is a particularly useful capability for generating such insights as it allows businesses to quickly review and understand user issues without listening through recordings or reading long transcripts. Recent advances in Large Language Models have made it possible to automatically generate useful summaries from call transcripts. In this post, we show how builders can use output from the Amazon Chime SDK Call Analyticsto create short call summaries using a Large Language Model (LLM). 

***
### Prerequisits
* Subscription to AWS Sagemaker Foundation Models
* (optional) Subscription to [cohere-gpt-medium](https://aws.amazon.com/marketplace/pp/prodview-6dmzzso5vu5my)
* Sagemaker Notebook Instance

### How it Works
We have provided a notebook that walks the user through (1) loading a transcript, (2) preparing it as a summarization task prompt for a Large Language Model, (3) submits the prompt to the model, and (4) saves the output as a summary. 

Several LLM options are available to users. We used Cohere in the notebook because it is available as a [SageMaker Model Package](https://aws.amazon.com/blogs/machine-learning/cohere-brings-language-ai-to-amazon-sagemaker/). To gain access to the LLM used in this blog, [Subscribe to Foundation Models](https://aws.amazon.com/sagemaker/jumpstart/getting-started/); in the AWS console, go to SageMaker and choose Jumpstart -> Foundation Models on the left toolbar. You will either have access and see the options, or you will need to Request Access and wait 24 hours. Once you have access to Foundation Models, subscribe to [cohere-gpt-medium](https://aws.amazon.com/marketplace/pp/prodview-6dmzzso5vu5my). Using this LLM is optional for the reader, as other LLMs are available.

The Notebook allows users to test access to the LLM and engineer prompts specific to their problem. Start a Notebook Instance of size ml.t3.medium, and navigate to Jupyter Lab on your notebook instance once available. Clone this repository using the Git dropdown menu in JupyterLab.

The Notebook has more instructions and explanations to follow.

### Additional Resources
* [amazon-chime-sdk-call-analytics-recorder](https://github.com/aws-samples/amazon-chime-sdk-call-analytics-recorder) gives an example of using this summarizer in a 
* [Cohere](https://cohere.com/)


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

