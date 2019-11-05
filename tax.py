def get_tax(taxable_income):

        #Step 1
        tax_difference = 0
        if taxable_income >= 300000:
            tax = 0.07 * 300000
        else:
            tax = 0.07 * taxable_income
            return tax

        tax_difference = taxable_income - 300000

        #step 2
        if tax_difference >= 300000:
            tax += (0.11 * 300000)
        else:
            tax += (0.11 * tax_difference)
            return tax

        tax_difference -= 300000

        #step 3
        if tax_difference >= 500000:
            tax += 0.15 * 500000
        else:
            # return 0.15* tax_difference
            tax += 0.15 * tax_difference
            return tax


        tax_difference -=500000

        # step4:

        if tax_difference >= 500000:
            tax += 0.19 * 500000
        else:
            tax += 0.19 * tax_difference
            return tax


        tax_difference -=300000
        #Step 5:

        if tax_difference >= 1600000:
            tax += 0.21 * 1600000
        else:
            tax += 0.21 * tax_difference

        tax_difference -= 300000

        # Step 6:

        if tax_difference >= 3200000:
            tax += 0.24 * tax_difference
            return tax
        else:
            tax += 0.24 * tax_difference
            return tax