#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(ggplot2)
library(dplyr)
library(tidyverse)
library(plotly)

# read data
df <- read.csv("https://raw.githubusercontent.com/charleyferrari/CUNY_DATA608/master/lecture3/data/cleaned-cdc-mortality-1999-2010-2.csv")
colnames(df)[1] <- 'cause_of_death'
# Define UI for application that draws a histogram
ui <- fluidPage(

    # Application title
    titlePanel("608_module3: Mortality data"),
    
    tabsetPanel(
        tabPanel(
            title = 'Question 1', 
            p(strong('Compare mortality rates from particular causes across different States')),
            hr(),
            sidebarLayout(
                sidebarPanel(
                     selectInput(inputId = 'cause', 
                                 label = 'Cause of death; ',
                                 choices = unique(df$cause_of_death), 
                                 selected = 'Certain infectious and parasitic diseases'
                                 )
                 ),
                 mainPanel(
                     plotlyOutput("barPlot1")
                     #plotOutput("barPlot")
                 )
            )
        ),
        tabPanel(
            title = 'Question 2',
            p(strong('Whether particular States are improving their mortality rates (per cause) faster than, or slower than, the national average')),
            hr(),
            sidebarLayout(
                sidebarPanel(
                    selectInput(
                        inputId = 'cause2',
                        label = 'Cause of death: ',
                        choices = unique(df$cause_of_death),
                    ),
                    selectInput(
                        inputId = 'state',
                        label = 'State: ',
                        choices = unique(df$State),
                    )
                    
                ),
                mainPanel(
                    plotlyOutput("barPlot2"),
                    hr(),
                    hr()
                    #plotlyOutput('linePlot')
                )
            )
        )
    ),
    mainPanel(p(""))
    
        
)


server <- function(input, output) {
    # question 1
    output$barPlot1 <- renderPlotly({
        
        df1 <- reactive(df %>% 
            filter(Year == 2010, cause_of_death == input$cause) %>% 
            select(cause_of_death, State, Crude.Rate) %>% 
            mutate(State = fct_reorder(State, Crude.Rate)))
        
        #df1() %>% 
        #    ggplot(aes(x = State, y = Crude.Rate)) +
        #    geom_bar(stat = 'identity') +
        #    theme_classic() +
        #    theme(axis.text.x = element_text(angle=90)) +
        #    labs(title = input$cause,
        #         y = 'mortality rate')
        
        plot_ly(df1(), x = ~Crude.Rate, 
                y = ~State,
                type = 'bar',
                name = 'State') %>% 
        layout(title = list(text = input$cause),
               xaxis = list(title = 'Mortality Rate'),
               yaxis = list(title = 'State')
               )
            

    })
    
    # question2
    output$barPlot2 <- renderPlotly({
        df2 <- reactive(df %>% 
            group_by(Year, cause_of_death) %>% 
            mutate(national_avg = round(sum(Deaths)/sum(Population) * 100000, 2)) %>% 
            filter(State == input$state, cause_of_death == input$cause2))
        
        #df2() %>%
        #    filter(State == input$state, cause_of_death == input$cause2) %>% 
        #    ggplot(aes(x = Year, y = Crude.Rate)) +
        #    geom_line() + 
        #    geom_line(aes(x = Year, y = national_avg)) +
        #    labs(y = 'mortality rate',
        #         title = paste0(input$cause2,' in ',input$state))
        
        
       plot_ly(df2(), x = ~Year, y = ~Crude.Rate,
               type = 'bar',
               name = 'State',
               text = ~Crude.Rate,
               textposition = 'auto') %>% 
           add_trace(y = ~national_avg,
                     type = 'bar',
                     name = 'US',
                     text = ~national_avg,
                     textposition = 'auto') %>% 
           layout(
               title = list(text = paste0(input$state, ": ", input$cause2)),
               xaxis = list(title = 'Year'),
               yaxis = list(title = 'Mortality Rate'),
               barmode = 'group'
           )
    })
    
    
}

# Run the application 
shinyApp(ui = ui, server = server)
