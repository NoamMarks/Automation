"""
Portal Client E2E Tests — Page Object Model

Tests the full CRUD lifecycle for Links, Domains, Tags, Messages, and Environments.
Each section uses a dedicated Page Object for all locators and interactions.
Performance is measured via the shared performance_step utility.
"""

import pytest
import uuid

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.links_page import LinksPage
from pages.domains_page import DomainsPage
from pages.tags_page import TagsPage
from pages.messages_page import MessagesPage
from pages.environments_page import EnvironmentsPage
from utils.performance import performance_step


# --- Shared test data fixture ---
@pytest.fixture(scope="session")
def test_data():
    return {}


class TestPortalClient:

    # ---------------------------------------------------------
    # Login & Navigation
    # ---------------------------------------------------------
    def test_login(self, page, extras):
        print("\n🔑 Starting Admin Login...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()

        with performance_step("Admin Login Action", extras, page=page, limit_ms=8000):
            login.click_login()

        login.wait_for_dashboard()

    def test_navigate(self, page, extras):
        print("\n🧭 Checking Navigation Menu...")
        nav = NavigationPage(page)

        with performance_step("Navigate to Content Worlds", extras, page=page, limit_ms=5000):
            nav.go_to_content_worlds()

        with performance_step("Navigate to Tags", extras, page=page, limit_ms=5000):
            nav.go_to_tags()

        with performance_step("Navigate to Messages", extras, page=page, limit_ms=5000):
            nav.go_to_messages()

        with performance_step("Navigate to Environments", extras, page=page, limit_ms=5000):
            nav.go_to_environments()

        with performance_step("Navigate to Links", extras, page=page, limit_ms=5000):
            nav.go_to_links()

    # ---------------------------------------------------------
    # Links CRUD
    # ---------------------------------------------------------
    def test_create_link(self, page, test_data, extras):
        name = f"TestLink_{uuid.uuid4().hex[:6]}"
        url = f"https://example.com/{uuid.uuid4().hex[:8]}"

        links = LinksPage(page)
        links.create_link(name, url, "Test link description")

        with performance_step("Create Link (Save)", extras, page=page, limit_ms=5000):
            links.click_save_and_confirm()

        links.verify_link_visible(name)
        test_data['link_name'] = name

    def test_update_link(self, page, test_data, extras):
        old_name = test_data.get("link_name", "TestLink")
        new_name = f"{old_name}_upd"

        links = LinksPage(page)
        links.update_link(old_name, new_name)

        with performance_step("Update Link", extras, page=page, limit_ms=5000):
            links.click_save_and_confirm()

        links.verify_link_visible(new_name)
        test_data["link_name"] = new_name

    def test_delete_link(self, page, test_data, extras):
        name = test_data.get("link_name", "TestLink_upd")

        links = LinksPage(page)
        links.delete_link(name)

        with performance_step("Delete Link", extras, page=page, limit_ms=5000):
            links.click_delete_and_confirm()

        links.verify_link_not_attached(name)

    # ---------------------------------------------------------
    # Domains (Content Worlds) CRUD
    # ---------------------------------------------------------
    def test_create_domain(self, page, test_data, extras):
        name = f"TestDomain{uuid.uuid4().hex[:4]}"
        nav = NavigationPage(page)
        nav.go_to_content_worlds()

        domains = DomainsPage(page)
        domains.create_domain(name)

        with performance_step("Create Domain", extras, page=page, limit_ms=5000):
            domains.click_save_and_confirm()

        domains.verify_domain_visible(name)
        test_data["domain_name"] = name

    def test_update_domain(self, page, test_data, extras):
        old_name = test_data.get("domain_name")
        assert old_name, "Missing domain name"
        new_name = f"TestDomain{uuid.uuid4().hex[:4]}"

        domains = DomainsPage(page)
        domains.update_domain(old_name, new_name)

        with performance_step("Update Domain", extras, page=page, limit_ms=5000):
            domains.click_save_and_confirm()

        domains.verify_domain_visible(new_name)
        test_data["domain_name"] = new_name

    def test_delete_domain(self, page, test_data, extras):
        name = test_data.get("domain_name")

        domains = DomainsPage(page)
        domains.delete_domain(name)

        with performance_step("Delete Domain", extras, page=page, limit_ms=5000):
            domains.click_delete_and_confirm()

        domains.verify_domain_not_visible(name)

    # ---------------------------------------------------------
    # Tags CRUD
    # ---------------------------------------------------------
    def test_create_tag(self, page, test_data, extras):
        tag_name = f"Tag{uuid.uuid4().hex[:5]}"
        nav = NavigationPage(page)
        nav.go_to_tags()

        tags = TagsPage(page)
        tags.create_tag(tag_name)

        with performance_step("Create Tag", extras, page=page, limit_ms=5000):
            tags.click_save_and_confirm()

        tags.verify_tag_visible(tag_name)
        test_data["tag_name"] = tag_name

    def test_update_tag(self, page, test_data, extras):
        old_name = test_data.get("tag_name")
        new_name = f"{old_name}upd"

        tags = TagsPage(page)
        tags.update_tag(old_name, new_name)

        with performance_step("Update Tag", extras, page=page, limit_ms=5000):
            tags.click_save_and_confirm()

        tags.verify_updated_tag_visible(new_name)
        test_data["tag_name"] = new_name

    def test_delete_tag(self, page, test_data, extras):
        tag_name = test_data.get("tag_name")

        tags = TagsPage(page)
        tags.delete_tag(tag_name)

        with performance_step("Delete Tag", extras, page=page, limit_ms=5000):
            tags.click_delete_and_confirm()

        tags.verify_tag_not_attached(tag_name)

    # ---------------------------------------------------------
    # Messages CRUD
    # ---------------------------------------------------------
    def test_create_message(self, page, test_data, extras):
        nav = NavigationPage(page)
        nav.go_to_messages()

        message_name = f"Msg_{uuid.uuid4().hex[:5]}"

        messages = MessagesPage(page)
        messages.create_message(message_name)

        with performance_step("Create Message", extras, page=page, limit_ms=5000):
            messages.click_save_and_confirm()

        messages.verify_message_visible(message_name)
        test_data["message_name"] = message_name

    def test_update_message(self, page, test_data, extras):
        old_name = test_data.get("message_name")
        new_name = f"{old_name}_upd"

        nav = NavigationPage(page)
        nav.go_to_messages()

        messages = MessagesPage(page)
        messages.update_message(old_name, new_name)

        with performance_step("Update Message", extras, page=page, limit_ms=5000):
            messages.click_save_and_confirm()

        messages.verify_message_updated(new_name)
        test_data["message_name"] = new_name

    def test_delete_message(self, page, test_data, extras):
        name = test_data.get("message_name")

        messages = MessagesPage(page)
        messages.delete_message(name)

        with performance_step("Delete Message", extras, page=page, limit_ms=5000):
            messages.click_delete_and_confirm()

        messages.verify_message_not_attached(name)

    # ---------------------------------------------------------
    # Environments CRUD
    # ---------------------------------------------------------
    def test_create_environment(self, page, test_data, extras):
        nav = NavigationPage(page)
        nav.go_to_environments()

        env_name = f"Env{uuid.uuid4().hex[:6]}"
        env_param = f"param{uuid.uuid4().hex[:6]}"

        envs = EnvironmentsPage(page)
        envs.create_environment(env_name, env_param)

        with performance_step("Create Environment", extras, page=page, limit_ms=5000):
            envs.click_save_and_confirm()

        envs.verify_environment_visible(env_name)
        test_data["env_name"] = env_name

    def test_update_environment(self, page, test_data, extras):
        old_name = test_data.get("env_name")
        new_name = f"{old_name}upd"

        envs = EnvironmentsPage(page)
        envs.update_environment(old_name, new_name)

        with performance_step("Update Environment", extras, page=page, limit_ms=5000):
            envs.click_save_and_confirm()

        envs.verify_environment_visible(new_name)
        test_data["env_name"] = new_name

    def test_delete_environment(self, page, test_data, extras):
        name = test_data.get("env_name")

        envs = EnvironmentsPage(page)
        envs.delete_environment(name)

        with performance_step("Delete Environment", extras, page=page, limit_ms=5000):
            envs.click_delete_and_confirm()

        envs.verify_environment_not_attached(name)