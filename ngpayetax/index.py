class PayeTax:
    def __init__(self, annual_taxable_income):
        """ 
        Taxable income: Taxable income refers to the base upon which an income tax system imposes tax
        This function accepts your yearly taxable income
        """
        self.tax= 0.0
        self.taxable_income = annual_taxable_income

    def annual(self):

            #Step 1
            tax_difference = 0
            if self.taxable_income >= 300000:
                self.tax= 0.07 * 300000
            else:
                self.tax= 0.07 * self.taxable_income
                return self.tax

            tax_difference = self.taxable_income - 300000

            #step 2
            if tax_difference >= 300000:
                self.tax+= (0.11 * 300000)
            else:
               self.tax += (0.11 * tax_difference)
               return self.tax

            tax_difference -= 300000

            #step 3
            if tax_difference >= 500000:
                self.tax+= 0.15 * 500000
            else:
                self.tax+= 0.15 * tax_difference
                return self.tax


            tax_difference -=500000

            # step4:

            if tax_difference >= 500000:
                self.tax+= 0.19 * 500000
            else:
                self.tax+= 0.19 * tax_difference
                return self.tax


            tax_difference -=300000
            #Step 5:

            if tax_difference >= 1600000:
                self.tax+= 0.21 * 1600000
            else:
                self.tax+= 0.21 * tax_difference

            tax_difference -= 300000

            # Step 6:

            if tax_difference >= 3200000:
                self.tax+= 0.24 * tax_difference
                return tax
            else:
                self.tax += 0.24 * tax_difference
                return self.tax


    def monthly(self):
        return self.annual()/12
        
