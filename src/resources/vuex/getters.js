export default {
    getAllClassroom(state) {
        return state.classrooms;
    },

    getClassroomDetail(state) {
        return state.classroomDetail;
    },

    getAllLecutres(state) {
        return state.lectures;
    },

    getAllPosts(state) {
        return state.posts;
    },

    isAuthenticated(state) {
        return state.auth.isAuthenticated;
    }
}