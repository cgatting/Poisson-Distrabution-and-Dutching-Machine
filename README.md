
# Automated Sports Betting Analysis System

This repository offers tools and scripts for automating sports betting analysis, pathway management, probability modeling, and strategy execution. Ideal for developers interested in building customizable sports betting automation, it supports varied betting strategies and integrates predictive modeling.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Scripts Overview](#scripts-overview)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project is a toolkit for automating sports betting, analyzing event data, predicting outcomes, and implementing strategies. It includes scripts for calculating odds, managing betting pathways, and using Poisson distribution to model score predictions, particularly useful for football.

## Features

- **Betting Pathway Management**: Organize bets with `BET ID PATHSWAYS.txt` by categories like "Match Winner," "Goals Over/Under," and "Exact Score."
- **Predictive Modeling**: Use Poisson distribution to calculate score probabilities.
- **Automated Betting**: Scripts to automate betting processes, manage outcomes, and apply various strategies.
- **Testing & Debugging**: Test scripts to validate betting logic.

## Requirements

- Python 3.8+
- Packages: `pandas`, `numpy`, `openpyxl`
- Additional requirements based on specific betting platform integrations.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/cgatting/Poisson-Distrabution-and-Dutching-Machine
   cd betting-analysis
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Configure Betting Pathways**: Edit `BET ID PATHSWAYS.txt` to match your betting platform.
2. **Run Betting Scripts**: Execute `main_bot.py` to start the automated betting process.
   ```bash
   python main_bot.py
   ```
3. **Test Functionality**: Use `test.py` for running tests to ensure scripts are working as expected.
   ```bash
   python test.py
   ```

## Scripts Overview

- **BET ID PATHSWAYS.txt**: Defines betting categories and conditions for streamlined organization.
- **Ducthing_Not_Working.py**: Manages betting pathways and debugging.
- **main_bot.py**: Core script to execute betting actions and manage results.
- **poisson-distribution-football-2.xlsx**: Provides score prediction based on Poisson distribution.
- **test.py**: Testing script for validating betting functions.
- **working_odds.py**: Assists with calculating and formatting odds.

## Contributing

Contributions are welcome! Fork this repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License.
