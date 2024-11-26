import apiClient from './api';

// Define the type for user registration data
export interface UserData {
    username: string;
    email: string;
    password: string;
}

// Define the type for login credentials
export interface LoginCredentials {
    username: string;
    password: string;
}

// Register a new user
export const registerUser = (userData: UserData) => {
    return apiClient.post('/register', userData)
        .then(response => {
            // Save the JWT token in localStorage or cookies
            localStorage.setItem('access_token', response.data.access_token);
            return response;
        });
};

// Log in a user
export const loginUser = (credentials: LoginCredentials) => {
    return apiClient.post('/login', credentials)
        .then(response => {
            // Save the JWT token in localStorage or cookies
            localStorage.setItem('access_token', response.data.access_token);
            return response;
        });
};

// Fetch all users (authenticated route)
export const fetchUsers = () => {
    return apiClient.get('/users', {
        headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`
        }
    });
};
