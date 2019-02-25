# Bootstrap_test_prep



1. CDN (content delivery(distribution) network)



2. css reset



3. Utilities

   1. Spacing (음수는 m만 가능) (브라우저 기본 rem은 16px)

      ![image](https://user-images.githubusercontent.com/45819975/53298545-faffb500-3872-11e9-833a-a8c9213cc72d.png)

   2. Color

      ![image](https://user-images.githubusercontent.com/45819975/53298662-7c0b7c00-3874-11e9-80e3-f1486cee8cb6.png)

      - text-primary
      - bg-primary
      - alert-primary
      - button-primary
      - navbar-dark

   3. Border

      - .border
      - .border .border-primary
      - .rounded
      - .rounded-circle
      - .rounded-pill

   4. Display

      - .d-block / inline / inline-block / none

   5. Position

      - .position-static / relative / absolute / fixed
      - .fixed-top
      - .fixed-bottom

   6. Text

      - .text-left/right/center
      - .font-weight-bold / bolder / light / lighter / normal
      - .font-italic



4. GRID system

   1. row-col

   2. Allignment

      1. vertical

         ```html
         <div class="container">
           <div class="row align-items-start">
             <div class="col">
               One of three columns
             </div>
             <div class="col">
               One of three columns
             </div>
           </div>
           <div class="row align-items-center">
             <div class="col">
               One of three columns
             </div>
             <div class="col">
               One of three columns
             </div>
           </div>
           <div class="row align-items-end">
             <div class="col">
               One of three columns
             </div>
             <div class="col">
               One of three columns
             </div>
           </div>
         </div>
         ```

      2. vertical - self

         ```html
         <div class="container">
           <div class="row">
             <div class="col align-self-start">
               One of three columns
             </div>
             <div class="col align-self-center">
               One of three columns
             </div>
             <div class="col align-self-end">
               One of three columns
             </div>
           </div>
         </div>
         ```

      3. horizontal

         ```html
         <div class="container">
           <div class="row justify-content-start">
             <div class="col-4">
               One of two columns
             </div>
             <div class="col-4">
               One of two columns
             </div>
           </div>
           <div class="row justify-content-center">
             <div class="col-4">
               One of two columns
             </div>
             <div class="col-4">
               One of two columns
             </div>
           </div>
           <div class="row justify-content-end">
             <div class="col-4">
               One of two columns
             </div>
             <div class="col-4">
               One of two columns
             </div>
           </div>
           <div class="row justify-content-around">
             <div class="col-4">
               One of two columns
             </div>
             <div class="col-4">
               One of two columns
             </div>
           </div>
           <div class="row justify-content-between">
             <div class="col-4">
               One of two columns
             </div>
             <div class="col-4">
               One of two columns
             </div>
           </div>
         </div>
         ```

         

      