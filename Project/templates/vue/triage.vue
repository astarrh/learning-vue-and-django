<template id="project-list-template">
  <h2>Projects</h2>
  <project-form @project-created="addProject"></project-form>
  <project-item
    v-for="project in projects"
    v-bind:key="project.id"
    v-bind:name="project.name"
  >[[ project.name ]]</project-item>
</template>

<template id="project-form-template">
  <form id="newProjectForm" @submit.prevent="createProject">
  <input id="newProjectName" v-model="newProjectName" placeholder="Name Project">
  <input class=button type="submit" value="Create Project">
  </form>
</template>

<template id="project-item-template">
  <div class="project-item">
    <h3>[[ project.name ]]</h3>
  </div>
</template>