# SBC Auto - Squad Builder Challenge Auto Solver

A full-stack web application designed to automate and optimize the solution process for Squad Builder Challenges (SBCs) in EA FC 24's Ultimate Team. 
SBC Auto significantly reduces the time and complexity involved in solving SBC puzzles by using advanced web scraping and a genetic algorithm to provide 
the most cost-effective squad configurations.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)

## Overview

EA FC Ultimate Team is a game mode that allows players to create squads using player cards from packs or the market. 
These squads can be used in competitive play or to solve puzzles known as Squad Builder Challenges (SBCs). SBC Auto aims to 
automate the solution process for these challenges by scraping user-owned player data and applying a genetic algorithm to find 
the optimal squad based on the SBC criteria.

## Features

- **Automated Data Gathering**: Uses Selenium to scrape user-owned player cards, capturing essential attributes such as ratings, positions, and more.
- **Genetic Algorithm**: Efficiently assembles squads that meet specific SBC requirements, optimizing for factors like team rating and chemistry.
- **Next.js Frontend**: A user-friendly interface developed with Next.js, TypeScript, and Tailwind CSS, allowing users to input SBC criteria and view optimal squad solutions.
- **Real-time Updates**: Utilizes Socket.IO for real-time feedback during the data scraping and squad assembly processes.
- **Backend Integration**: Flask API that connects frontend inputs with backend processing for seamless data flow and interaction.

## Technologies Used

- **Frontend**: Next.js, TypeScript, Tailwind CSS, Chakra UI
- **Backend**: Flask, Python
- **Web Scraping**: Selenium
- **Database**: SQLite, Pandas
- **Real-time Communication**: Socket.IO
