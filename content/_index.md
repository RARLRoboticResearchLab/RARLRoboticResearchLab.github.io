---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        Robotics and Automation
        Research Lab
      image:
        filename: welcome.jpg
      text: |
        <br>
        The Robotics and Automation Research Laboratory (RARL) was established to innovate, design, and develop robots, with a particular focus on service robots and automation projects. Beyond research, RARL aims to provide consultation and support to industries seeking advanced automation solutions.
      text2: |
        <br>
        
  - block: slider
    content:
      slides:
        - title: 
          content: 
          align: 
          background:
            image:
              # Specify an image from `assets/media/`
              # or delete the image section to remove it
              filename: RARL_Certificate of Technical Sponsor at IAR 2024--RARL.jpg
              size: contain
              filters:
                brightness: 1.0
            position: center
            color: '#666'
        - title: 
          content: 
          align: center
          background:
            image:
              # Specify an image from `assets/media/`
              # or delete the image section to remove it
              filename: RARL_IEID 2025.jpg
              size: contain
              filters:
                brightness: 1.0
            position: center
            color: '#555'
        - title: 
          content: 
          align: center
          background:
            image:
              # Specify an image from `assets/media/`
              # or delete the image section to remove it
              filename: RARL_MSIM 2025.jpg
              filters:
                brightness: 1.0
              size: contain
            position: left
            color: '#333'
            

          # link:
          #   icon: graduation-cap
          #   icon_pack: fas
          #   text: Join Us
          #   url: ../contact/
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: '600px'
      # Make the slides full screen within the browser window?
      is_fullscreen: false
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 2000

  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'
  
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: coders.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

  

  - block: collection
    content:
      title: Latest Publications
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article-journal'
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
