# logistic-optimization
Delivery drivers location optimization with Causal Inference 

**Table of Content**
* [Project Overview](#project-overview)
* [Data](#data)
* [Installation Guide](#installation-guide)
* [Project Structure](#project-structure)
* [LICENCE](#licence)
* [Contributers](#contributors)

## Project Overview
The main objective of this project to work on its data to help it understand the primary causes of unfulfilled requests as well as come up with solutions that recommend drivers locations that increase the fraction of complete orders. Since drivers are paid based on the number of requests they accept, your solution will help our client business grow both in terms of client satisfaction and increased business. 

## Data
There is two datasets available for this project.

The first one is the table that contains information about the completed orders
| # | Column           | Non-Null Count  | Dtype     |
|---|------------------|-----------------|-----------|
| 0 | Trip ID          | 536020 non-null | int64     |
| 1 | Trip Origin      | 536020 non-null | address   |
| 2 | Trip Destination | 536020 non-null | address   |
| 3 | Trip Start Time  | 534369 non-null | timestamp |
| 4 | Trip End Time    | 536019 non-null | timestamp |
 
The second one is the table that contains delivery requests by clients (completed and unfulfilled) 
| # | Column        | Non-Null Count   | Dtype   |
|---|---------------|------------------|---------|
| 0 | id            | 1557740 non-null | int64   |
| 1 | order_id      | 1557740 non-null | int64   |
| 2 | driver_id     | 1557740 non-null | int64   |
| 3 | driver_action | 1557740 non-null | object  |
| 4 | lat           | 1557740 non-null | float64 |
| 5 | lng           | 1557740 non-null | float64 |
| 6 | created_at    | 0 non-null       | float64 |
| 7 | updated_at    | 0 non-null       | float64 |


## Installation Guide
```
git clone https://github.com/andyalex234/logistic-optimization.git
cd logistic-optimization
pip install -r requirements.txt
```

## Project Structure

### LICENCE
 MIT
#### Contributors

<a href = "https://github.com/andyalex234">
  <img src="https://contrib.rocks/image?repo=andyalex234/logistic-optimization" />
  Andenet Alexander
</a>

> any type of contribution is welcomed. [Fork](https://github.com/andyalex234/logistic-optimization/fork), apply your changes and make a [pull request](https://github.com/andyalex234/logistic-optimization/pull).

