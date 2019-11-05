# Nigeria Paye Tax Calculator

Ngpayetax is a very simple Pay As You Earn module. It allows you to easily calculated your employees tax according to the recent tax table.

This module is constantly updated to keep you tax compliant.


<img src="https://circleci.com/gh/ezesundayeze/paye-tax.svg?style=svg&circle-token=7ce2cadfc01b5f01377b79874fc4e1732c56c437" alt="circle ci">

## Installation

```bash

pip install git+https://github.com/ezesundayeze/paye-tax.git@80371bb304ddd2ef6bd5a2e76e30b4b22e4c20f8

```

## Usage

```python
from ngpayetax import PayeTax
annual_taxable_income = 1250000
payetax = PayeTax(annual_taxable_income)

#Get the annual tax
payetax.annual() #returns float

#Get monthly tax
payetax.monthly() # returns float
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)