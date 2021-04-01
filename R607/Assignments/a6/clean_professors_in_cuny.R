library(rvest)
library(tidyverse)
library(stringr)

data <- read_html("http://www.cuny.edu/about/alumni-students-faculty/faculty/distinguished-professors/")

# extract the info of each professor

info <- data %>%
  html_nodes("td") %>% 
  html_node("p") %>%
  html_text() %>%
  na.omit()

# extract name
name <- data %>%
  html_nodes("td") %>%
  html_nodes("h3") %>%
  html_text() %>%
  na.omit()

# extract college
college <- info %>% str_extract_all("^College: .*Department")
college <- college %>% str_remove_all("College: ")
college <- college %>% str_remove_all("Department")

# extract department
department <- info %>% str_extract_all("Department: .*Email")
department <- department %>% str_remove_all("Department: ")
department <- department %>% str_remove_all("Email")

# extract email
email <- info %>% str_extract_all("Email: [a-zA-Z0-9._-]+@([a-zA-Z0-9_-]+\\.)+(org|edu|com|net)")
email <- email %>% str_remove_all("Email: ")

# extract office phone number
office_phone <- info %>% str_extract_all("\\(?\\d{3}\\)?[.-]? *\\d{3}[.-]? *[.-]?\\d{4}")
office_phone <- office_phone %>% str_extract_all("^\\(?\\d{3}\\)?[.-]? *\\d{3}[.-]? *[.-]?\\d{4}$")
office_phone[office_phone == "character(0)"] <- "NA"
office_phone <- unlist(office_phone)

df <- data.frame(name = name, college = college, department = department, email = email, office_phone = office_phone)


write.csv(df, "~/desktop/R/R607/tidyverse_git/professors_in_cuny.csv", row.names = FALSE)











