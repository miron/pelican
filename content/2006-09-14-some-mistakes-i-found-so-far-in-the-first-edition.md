Title: Mistakes in Agile Web Programming with Ruby on Rails
Date: 2006-09-14
Category: Ruby
Tags: code, ruby, rubyOnRails, rails, code
Slug: Some mistakes I found so far in the first edition
Summary: to err is human

Enclosed are snippets from Agile Web Programming with Ruby on Rails.


File 65:

    :::ruby
    %r{^http:.+\.(gif|jpg|png)$}i

changed to 

    :::ruby
    %r{\.(gif|jpg|png)$}i

Now i can save the pictures in the projects/images folder as suposed in the book and not somewhere at the internet.

File 67: 

    
    :::ruby
    :confirm => "Are you sure?" %>

changed to 

    :::ruby
    :confirm => "Are you sure?", 
    :post => true %>

Now i can delete the products too.
