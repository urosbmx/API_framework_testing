# Python Automation Framework for API Testing

This repository contains a Python-based automation framework for testing APIs, integrated with GitHub Actions for continuous integration and with Jira for issue tracking and project management.

## Features

- **API Testing**: The framework includes tools and utilities to perform automated testing of APIs.
- **GitHub Actions Integration**: Automated testing is triggered using GitHub Actions, ensuring continuous integration and validation of code changes.
- **Jira Integration**: Issues and tasks related to API testing and automation can be tracked and managed using Jira.

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/urosbmx/API_framework_testing
   ```

2. Navigate to the project directory:

   ```bash
   cd API_framework_testing
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your GitHub Actions workflow by creating a `.github/workflows` directory and adding a workflow YAML file that triggers your tests manually.

5. Configure the Jira integration by providing your Jira API credentials and project details in the `.env` file.

## Usage

### Running Tests Locally

You can run the automated tests locally using the following command:

```bash
pytest --jira-xray --cloud --client-secret-auth
```

### GitHub Actions

The GitHub Actions workflow is configured to trigger automated tests on specific events (e.g., push to `main` branch, pull requests). Ensure that your workflow file (`main.yml` or similar) is correctly set up in the `.github/workflows` directory.

### Jira Integration

To integrate with Jira, make sure you have valid API credentials and project details. Update the `.env` file with your Jira configuration.

### Test Reporting in Jira with pluging [pytest-jira-xray](https://pypi.org/project/pytest-jira-xray/)
![Jira Integration](https://i.ibb.co/8Y8q3VC/Screenshot-2024-04-09-at-23-02-49.png)

## Contributing

We welcome contributions to improve and extend this automation framework. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature_branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes to the branch (`git push origin feature_branch`).
5. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Contact

For any inquiries or support, please contact [Your Name](mailto:your_email@example.com).
